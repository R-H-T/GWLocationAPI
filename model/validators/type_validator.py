# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"


class TypeValidator(object):
    """ Type Validator """
    @staticmethod
    def check_string(value, value_name):
        if value is not None and type(value) is not str:
            raise TypeError('`{}`\'s type is invalid.'.format(value_name))

    @staticmethod
    def check_list(value, value_name):
        if value is not None and type(value) is not list:
            raise TypeError('`{}`\'s type is invalid.'.format(value_name))
