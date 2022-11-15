# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:46:23 2022

@author: V

Description:
    Write a Python program that prints a version of the string s with all commas replaced by dots.

Expected Output:
    Input: "Hello, World", "3,456,344"
    Output: "3.456.344"
"""
# Challenge Change Commas by Dots
print("Solution Change Commas by Dots")

# Option 1

s = "Hello, World!"
new_s = ""

COMMA = ","
DOT = "."

for char in s:
    if char == COMMA:
        new_s += DOT
    else:
        new_s += char
print(new_s)


# Option 2
s1 = "Hello, World"
print(s.replace(COMMA, DOT))
