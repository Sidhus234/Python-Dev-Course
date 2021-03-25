# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:02:41 2021

@author: sidhu
"""

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# == checks for equality

print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])

print(True is True)
# is checks for values stored in memory
print('1' is '1')
# is can't compare two data strucutres as they are created in different memory space
