# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:59:03 2022

@author: V

Description:
    Write a Python program that checks if the string s contains all the letters in the aplphabet (case-insensitive, so "A" should be equivalent to "a")
    If is does, print True. Else, print False
    Before comparing the characters, you should convert the string to lowercase.
    If the string contains spaces, ignore them before finding the result.
    You may assume that the string doesn't contain any other symbols, only spaces (possibly).
    Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz'

Expected Output:
    Input: "abcdefghijklmnopqrstuvwxyz", "The quick brown fox jumps over the lazy dog", "Hello"
    Output: True, True, False
    
Hints:
    To use a constant with all letters of the alphabet, you may use string.ascii_lowercase from the string module. You can import this module by writing import string at the top of your script.
    It can also be helpful to use sets in this problem.
"""
import string
# Challenge Check if String Contains All Letters in the Alphabet
print("Solution Check if String Contains All Letters in the Alphabet")

# Option 1
s = "The quick brown fox jumps over the lazy dog"
SPACE = " "


set_s = set(s.lower()) # Lowercase

if SPACE in set_s:
    set_s.remove(" ") # Remove spaces from the set


# Convert the string to a set to remove duplicate
# characters and order. Compare this set with 
# the set of letters inn the constant

print(set_s == set(string.ascii_lowercase))

# Option 2 use not in 

import string
s1 = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for char in string.ascii_lowercase:
    if char not in s1.lower():
        is_pangram = False
        break

print(is_pangram)





