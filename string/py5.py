# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:43:30 2022

@author: V

Description:
    Write a Python program that prints the string s without the characters located at even indices
    If the string is empty or only has one character, print it intact.

Exected Output:
    Input: "Coding", "Pizza", "Python", "A", ""
    Output: "oig", "iz", "yhn", "A", ""
"""
# Challenge Remove Characters at Even Indices
print('Solution Remove Characters at Even Indices')
# Option 1
# C o d i n g
# 0 1 2 3 4 5
# oig 1 3 5
s = 'Coding'
new_s= ''
for i in range(len(s)): # range(len(s)) 0, 1, 2, ... len(s) - 1
    if i % 2 != 0:
        new_s += s[i]
print(new_s)

# Option 2
new_s1 = ''
for i in range(1, len(s), 2):
    # print(range(1, len(s), 2))
    new_s1 += s[i]
print(new_s1)
    
