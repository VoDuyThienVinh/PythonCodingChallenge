# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 18:08:37 2022

@author: V

Description:
    Write a Python program that check if a string only contains numbers.
    If is does, print True. Else, print False

Excepted Output:
    Input: "Hello", "4567", "Hello59", ""
    Output: "False", "True", "False", "False"

Hints:
    The .isdigit() method returns True if all the characters in the string are digits
"""
# Challenge Check if a String Only Contains Numbers
print('Solution Check if a String Only Contains Numbers')
s = 'Hello59'
print(s.isdecimal())
print(s.isdigit())


