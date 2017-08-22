from camel import Camel

class CodeStyle(type):
    """
    https://habrahabr.ru/post/145835/
    """
    def __new__(cls, name, bases, dct):

        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        camelcase_attr = dict((name.Camel(), value) for name, value in attrs)

        return type.__new__(cls, name, bases, camelcase_attr)
#         return super(CodeStyle, cls).__new__(cls, name, bases, camelcase_attr)


# class MyAwesomeClass(metaclass = CodeStyle('CamelCase')):
#     def some_method(self):
#         pass

class MyAwesomeClass():
    def __init__(self):
        pass

    @staticmethod
    def some_method(self):
        return 'Hello'

# print(MyAwesomeClass.SomeMethod)
print(MyAwesomeClass.some_method())
