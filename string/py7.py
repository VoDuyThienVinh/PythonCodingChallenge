# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 18:22:25 2022

@author: V

Description
    Write a Python program that prints the string s without the characters at index n.
    If the index n is out of range, print the string s intact
    If the string s is empty, print the string s intact.

Expected Output
    Input: "Hello", "World", "Dog", ""
    n: 1,3,15,2
    Output: "Hllo", "Word", "Dog", ""
"""
# Challenge Remove nth Character from a String
print('Solution Remove nth Character from a String')

# Option 1
s = "Hello" # len(s) -> 5 
n = 1 # 0 1 2 3 4

if(len(s) == 0 or n > len(s)):
    print(s)
else:
    new_s = ''
    for i in range(len(s)):
        if i != n :
            new_s += s[i]
    print(new_s)
        
# Option 2
s1 = "Hello"
n1 = 1
if (not s) or n > len(s):
    print(s1)
else:
    new_s1 =''
    for i in range(len(s)):
        if i != n1:
            new_s1 += s1[i]
    print(new_s1)



s2 = '1'
print(not s2)




        
        
    
