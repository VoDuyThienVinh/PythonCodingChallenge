# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:28:38 2022

@author: V

Description:
    Write a Python program that prints the character at index i in the string s.
    If the index is out range, the prgram should print "i is out of range"
    If the string is empty, the program should print "Empty String"

Expected Output:
    String: "Hello", "Pizza", "", "World"
    i: 2, 4, 3, 15
    Output: "l", "a", "Empty String", "l is out of range"
"""

# 2. Challenge Print the Character at a Specific Index
print('Solution Print the Character at a Specific Index')

s = 'Hello'  
i = 12
indexTotal = len(s)


if(len(s) == 0):
    print('empty string')
elif (i < len(s)):
    print(s[i])
else:
    print('l is out of range')