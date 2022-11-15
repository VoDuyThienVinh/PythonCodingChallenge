# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:27:59 2022

@author: V

Description:
    Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
    curr_char and new_char are variables that contain strings with a single character.
    You may assume that new_char will not be an empty string.
    The match must me case-sensitive (do not replace lowercase letters if curr_char is uppercase).
    If no match is found, print the initial string

Expected Output:
    String: "Hello", "World", "Python", "Python"
    curr_char: "l", "W", "P", "p"
    new_char: "s", "A", "x", "a"
    Output: "Hesso", "Aorld", "xython", "Python"
"""

# Challenge Replace a Character in a String 
print('Solution Replace a Character in a String')
# Option 1
s = 'Hello'
new_s = ''
curr_char = 'l'
new_char = 's'

for char in s:
    if char == curr_char:
        char = new_char
    new_s += char
        
print(new_s)

# Option 2
s1 = "Python"
curr_char1 = 'P'
new_char1 = 'a'

print(s1.replace(curr_char1, new_char1))

