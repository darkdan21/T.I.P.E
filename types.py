#!/bin/python

def tipe(*dargs):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print(args)
            print(kwargs)
            print(dargs)
            print(function)
            result = function(*args, **kwargs)
            print(result)
            return result
        return wrapper
    return real_decorator
