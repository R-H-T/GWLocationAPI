# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"

from view import HomeView


class IndexController:
    def __init__(self, title, args=None):
        self.title = title
        self.args = args

    def render_view(self):
        """Renders the main view"""
        view = HomeView(self.title, self.args)
        return view.render()

    def add_to_args(self, arg):
        """Adds an extra argument for the main view.
        Returns True or False indicating success or failure."""
        if self.args is None:
            self.args = arg
            return True
        self.args.include(arg)
        return self.args.contain(arg)
