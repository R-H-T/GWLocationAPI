# Scripts Directory

This directory contains automation scripts for maintaining the GWLocationAPI project.

## Available Scripts

### `merge-dependabot-prs.sh`
Automatically approves and merges Dependabot pull requests in the correct order to avoid conflicts and ensure security updates are applied systematically.

**Usage:**
```bash
# Dry run (see what would be merged without actually merging)
./scripts/merge-dependabot-prs.sh true

# Execute the merge process
./scripts/merge-dependabot-prs.sh false
```

**Prerequisites:**
- GitHub CLI (`gh`) installed and authenticated
- Write permissions to the repository
- Internet connection for API calls

**Features:**
- Prioritizes security-critical updates
- Handles merge conflicts gracefully
- Provides detailed progress reporting
- Includes rollback information
- Supports dry-run mode for testing

For detailed information, see [docs/DEPENDABOT_MERGE_GUIDE.md](../docs/DEPENDABOT_MERGE_GUIDE.md).