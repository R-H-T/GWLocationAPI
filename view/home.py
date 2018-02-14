# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"

from view import View


class HomeView(View):
    def __init__(self, title, args=None):
        super().__init__()
        self.title = title
        self.args = args

    def render(self, template_name="view", values=None, options=None):
        """Rendering our title view template"""
        values = {'title': self.title}
        if self.args is not None and self.args['content'] is not None:
            values['content'] = self.args['content']
        return super().render("home_view", values, options)
