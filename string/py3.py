# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:11:43 2022

@author: V

Description:
    Write a Python Program that prints the reversed version of a string.
    The program must preserve uppercase and lowercase letters.
    If the string is empty, print it intact.

Expected Output
    Input: "Hello", "Wo"
    Output: "olleH", "oW"

"""
# Challenge Reverse a String
print('Solution Reverse a String')

# string[start:stop:step]
# Option 1
s = 'Hello'

# Option 2
s1 = 'Hello'[::-1]

# Option 3
s2 = s[::-1]

# Option 4
# reversed("Hello") -> ["o", "l", "l", "e", "H"]
# "".join(["o", "l", "l", "e", "H"])
s3 = "".join(reversed(s))
print(s3)
