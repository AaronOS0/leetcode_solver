#!/usr/bin/env python

# Demo of Recursion

# print first, then call itself
def f1(x):
    if x > 0:
        print(x)
        f1(x-1)


f1(3)


# call itself first, then print
def f2(x):
    if x > 0:
        f2(x-1)
        print(x)


f2(3)
