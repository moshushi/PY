import pytest
from MetaCamel import CodeStyle

def test_One():
    class MyAwesomeClass(metaclass=CodeStyle):
        def some_method(self):
            return 'bip'

    A = MyAwesomeClass()

#     assert A.SomeMethod() == 'bip'
    assert hasattr(A, 'SomeMethod')
