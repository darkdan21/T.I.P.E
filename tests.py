#!/bin/python
from types import *
from tests.test_functions import *

def run_tests(): 

    done = 0

    try:
        single_integer(1)
        double_integer(1,1)
        triple_integer(1,1,1)
        single_string("test")
        int_string_int(1,"test",1)
        print("Positive checking successful")
        done+=1
    except Exception as e:
        print("Tests failed because:",e)

    try:
        try:
            single_integer("p")
            print("Test failed")
        except TipeArgumentTypeError:
            pass

        try:
            double_integer("p","p")
            print("Test failed")
        except TipeArgumentTypeError:
            pass

        try:
            double_integer(1,"p")
            print("Test failed")
        except TipeArgumentTypeError:
            pass

        try:
            double_integer("p",1)
            print("Test failed")
        except TipeArgumentTypeError:
            pass

        try:
            single_integer(1,1)
            print("Test failed")
        except TipeArgumentLengthError:
            pass

        try:
            single_integer("p","p")
            print("Test failed")
        except TipeArgumentTypeError:
            pass
        except TipeArgumentLengthError:
            pass

        done+=1
        print("Negative checking successful")
    except Exception as e:
        print("Tests failed because:",e)

    if(done == 2):
        print("All tests succesful")

if __name__ == "__main__":
    run_tests()
