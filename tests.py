#!/bin/python
import types
from tests.test_functions import *

def run_tests(): 
    try:
        single_integer(1)
        double_integer(1,1)
        triple_integer(1,1,1)
        single_string("test")
        int_string_int(1,"test",1)
    except Exception as e:
        print("Tests failed because:",e)



if __name__ == "__main__":
    run_tests()
