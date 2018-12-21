#!/bin/python
from types import tipe

@tipe(int)
def single_integer(x):
    return 0

@tipe(int,int)
def double_integer(x,y):
    return 0

@tipe(int,int,int)
def triple_integer(x,y,z):
    return 0

@tipe(str)
def single_string(s):
    return 0

@tipe(int, str, int)
def int_string_int(x,s,y):
    return 0
