#!/usr/bin/python3

from functools import wraps


def debug(func):
    @wraps(func)
    def wrapper(*a, **kw):
        print("Function ", func.__name__, " has been called.")
        return func(*a, **kw)
    return wrapper

def debug_methods(cls):
    for key, value in vars(cls).items():
        if callable(value):
            setattr(cls, key, debug(value))

# @debug_methods
class Foo:
    def __init__(self, name):
        self.name = name
    @debug
    def bar(self):
        return ""

# print(dir(Foo))
foo = Foo(name="marcus")
foo.bar()
print(foo.__dict__)
