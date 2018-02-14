# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"

from flask import render_template


class View:
    def __init__(self, x=0, y=0, width=100, height=100):
        self.frame = {'x': x, 'y': y, 'width': width, 'height': height}

    def render(self, template_name="view", values=None, options=None):
        """Renders the view with the provided template name."""
        return render_template("%s.html" % template_name,
                               frame=self.frame,
                               values=values,
                               options=options)
