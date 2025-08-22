#!/bin/bash

# Dependabot PR Auto-Merger Script
# This script systematically approves and merges Dependabot PRs in order of security priority

set -e

# Configuration
REPO_OWNER="R-H-T"
REPO_NAME="GWLocationAPI"
DRY_RUN=${1:-false}

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if gh CLI is installed and authenticated
if ! command -v gh &> /dev/null; then
    echo -e "${RED}❌ GitHub CLI (gh) is not installed. Please install it first.${NC}"
    exit 1
fi

# Check authentication
if ! gh auth status &> /dev/null; then
    echo -e "${RED}❌ Not authenticated with GitHub CLI. Run 'gh auth login' first.${NC}"
    exit 1
fi

echo -e "${BLUE}🤖 Dependabot PR Auto-Merger${NC}"
echo -e "${BLUE}Repository: ${REPO_OWNER}/${REPO_NAME}${NC}"
echo -e "${BLUE}Dry Run: ${DRY_RUN}${NC}"
echo ""

# Define PRs in merge order (security-critical first, then dependencies)
declare -a PR_ORDER=(
    "15:SQLAlchemy 1.2.2 to 1.2.19 - Database security and stability"
    "14:urllib3 1.22 to 2.5.0 - Critical HTTP security vulnerabilities"
    "11:requests 2.18.4 to 2.32.4 - Critical HTTP security vulnerabilities" 
    "10:certifi 2022.12.7 to 2024.7.4 - Certificate authority updates"
    "13:Werkzeug 0.14.1 to 3.0.6 - Flask framework security"
    "12:Jinja2 2.10 to 3.1.6 - Template engine security"
    "9:gunicorn 19.7.1 to 23.0.0 - Web server security and performance"
    "5:httplib2 0.10.3 to 0.19.0 - HTTP library security (older)"
    "4:cryptography 2.1.4 to 3.2 - Cryptographic library security (older)"
)

merge_pr() {
    local pr_number=$1
    local description=$2
    
    echo -e "${BLUE}📋 Processing PR #${pr_number}: ${description}${NC}"
    
    # Check if PR exists and get details
    local pr_info
    if ! pr_info=$(gh pr view $pr_number --repo "${REPO_OWNER}/${REPO_NAME}" --json state,author,title 2>/dev/null); then
        echo -e "${YELLOW}⚠️ PR #${pr_number} not found or not accessible${NC}"
        return 1
    fi
    
    local pr_state=$(echo "$pr_info" | jq -r '.state')
    local pr_author=$(echo "$pr_info" | jq -r '.author.login')
    local pr_title=$(echo "$pr_info" | jq -r '.title')
    
    # Skip if not open
    if [ "$pr_state" != "OPEN" ]; then
        echo -e "${YELLOW}⏭️ Skipping PR #${pr_number} - not open (${pr_state})${NC}"
        return 0
    fi
    
    # Skip if not from Dependabot
    if [ "$pr_author" != "dependabot[bot]" ]; then
        echo -e "${YELLOW}⏭️ Skipping PR #${pr_number} - not from Dependabot (${pr_author})${NC}"
        return 0
    fi
    
    echo -e "${GREEN}✅ Found Dependabot PR: ${pr_title}${NC}"
    
    if [ "$DRY_RUN" = "true" ]; then
        echo -e "${BLUE}🔍 [DRY RUN] Would approve and merge PR #${pr_number}${NC}"
        return 0
    fi
    
    # Approve the PR
    echo -e "${BLUE}👍 Approving PR #${pr_number}...${NC}"
    if gh pr review $pr_number --approve --body "Auto-approving Dependabot security and dependency update" --repo "${REPO_OWNER}/${REPO_NAME}"; then
        echo -e "${GREEN}✅ Successfully approved PR #${pr_number}${NC}"
    else
        echo -e "${RED}❌ Failed to approve PR #${pr_number}${NC}"
        return 1
    fi
    
    # Merge the PR with squash merge
    echo -e "${BLUE}🔀 Merging PR #${pr_number}...${NC}"
    if gh pr merge $pr_number --squash --delete-branch --repo "${REPO_OWNER}/${REPO_NAME}"; then
        echo -e "${GREEN}✨ Successfully merged PR #${pr_number}${NC}"
        echo ""
        sleep 2 # Brief pause between merges
        return 0
    else
        echo -e "${RED}❌ Failed to merge PR #${pr_number}${NC}"
        return 1
    fi
}

# Main execution
echo -e "${BLUE}🚀 Starting Dependabot PR merge process...${NC}"
echo ""

success_count=0
failed_count=0
skipped_count=0

for pr_entry in "${PR_ORDER[@]}"; do
    IFS=':' read -r pr_number description <<< "$pr_entry"
    
    if merge_pr "$pr_number" "$description"; then
        if [ "$DRY_RUN" = "true" ]; then
            ((success_count++)) || true
        else
            # Check if it was actually merged (not skipped)
            pr_state=$(gh pr view $pr_number --repo "${REPO_OWNER}/${REPO_NAME}" --json state --jq '.state' 2>/dev/null || echo "MERGED")
            if [ "$pr_state" = "MERGED" ]; then
                ((success_count++)) || true
            else
                ((skipped_count++)) || true
            fi
        fi
    else
        ((failed_count++)) || true
    fi
done

echo ""
echo -e "${BLUE}📊 Final Summary:${NC}"
echo -e "${GREEN}✅ Successful merges: ${success_count}${NC}"
echo -e "${RED}❌ Failed merges: ${failed_count}${NC}"
echo -e "${YELLOW}⏭️ Skipped PRs: ${skipped_count}${NC}"

# List remaining Dependabot PRs
echo ""
echo -e "${BLUE}🔍 Checking for remaining Dependabot PRs...${NC}"
if remaining_prs=$(gh pr list --author "dependabot[bot]" --state open --repo "${REPO_OWNER}/${REPO_NAME}" --json number,title 2>/dev/null); then
    if [ "$(echo "$remaining_prs" | jq length)" -gt 0 ]; then
        echo -e "${YELLOW}⚠️ Remaining open Dependabot PRs:${NC}"
        echo "$remaining_prs" | jq -r '.[] | "  - PR #\(.number): \(.title)"'
    else
        echo -e "${GREEN}🎉 All Dependabot PRs have been processed!${NC}"
    fi
else
    echo -e "${RED}❌ Failed to check for remaining PRs${NC}"
fi

echo ""
if [ "$failed_count" -gt 0 ]; then
    echo -e "${RED}❌ Some merges failed. Please review the output above.${NC}"
    exit 1
else
    echo -e "${GREEN}🎉 Dependabot PR merge process completed successfully!${NC}"
    exit 0
fi