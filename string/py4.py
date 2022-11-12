# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:15:00 2022

@author: V

Description:
    Write a Python program that prints the first and last three characters of the string s as a single string.
    If the string has less than six characters, print an empty string (blank output).
    
Expected Output
    Input: "Blue", "Wonderful", "Amazing"
    Output: "", "Wonful", "Amaing"
"""
# Challenge First and Last Three Characters of a String
print('Solution First and Last Three Characters of a String')

# Option 1
s = 'Wonderful' # 0 1 2 3 4 5 6 7 8
print(len(s)) # 9

if(len(s) < 6):
    print('Empty string')
else:
    print(s[0:3] + s[-3:])
    
# Option 2
if(len(s) < 6):
    print('');
else:
    new_string = s[:3] + s[len(s) - 3:]
    print(new_string)
    
# Option 3
num_chars = 3
if(len(s) < num_chars*2):
    print('')
else:
    new_string1 = s[:num_chars] + s[len(s) - num_chars:]
    print(new_string1)




