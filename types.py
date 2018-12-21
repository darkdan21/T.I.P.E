#!/bin/python

class TipeError(TypeError):
    pass

class TipeArgumentLengthError(TipeError):
    pass

class TipeArgumentTypeError(TipeError):
    pass

def tipe(*dargs):
    def real_decorator(function):
        def wrapper(*args):
            if len(args) !=  len(dargs):
                raise TipeArgumentLengthError("Tipe decorator supplied with different number of arguments than the function")
            for i in range(0,len(args)):
                if type(args[i]) != dargs[i]:
                    raise TipeArgumentTypeError("Wrong arguments supplied to function")

            result = function(*args)
            return result
        return wrapper
    return real_decorator
