# -*- coding: utf-8 -*-

u"""
Задание: Написать фабрику метакласса, которая будет возвращать метакласс,
который будет приводить стиль наименования всех методов и свойств класса
к заданному
"""

from camel import Camel

class CodeStyle(type):
    """
    https://habrahabr.ru/post/145835/
    """
    def __new__(cls, name, bases, dct):

        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        camelcase_attr = dict((Camel(name), value) for name, value in attrs)

        return super(CodeStyle, cls).__new__(cls, name, bases, camelcase_attr)

# class Foo(metaclass=CodeStyle):
#     bar = 'bip'

# f = Foo()
# print(f.Bar)

class MyAwesomeClass(metaclass=CodeStyle):
    def some_method(self):
        pass

print(MyAwesomeClass.SomeMethod)
