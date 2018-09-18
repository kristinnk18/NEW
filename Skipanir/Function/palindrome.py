# A palindrome is a word, phrase, number, or other sequence of characters which reads the same 
# backward as forward, such as madam or racecar. Sentence-length palindromes may be written when 
# allowances are made for adjustments to capital letters, punctuation, and word dividers, 
# such as "A man, a plan, a canal, Panama!", "Was it a car or a cat I saw?" or "No 'x' in Nixon".
 
# Write a function that takes a string as an argument and returns True if the string is a 
# palindrome and False otherwise.
 
# Also write code that calls the function with the input as an argument and prints out the 
# appropriate message.

# Example input/output:

# Enter a string: No 'x' in Nixon.
# "No 'x' in Nixon." is a palindrome.

# Enter a string: blabla
# "blabla" is not a palindrome.

import string

bad_chars = string.punctuation + string.whitespace

def is_palindrome(original_str):
    modified_str = original_str.lower()

    for char in modified_str:
        if char in bad_chars:
            modified_str = modified_str.replace(char, '')

    if modified_str == modified_str[::-1]:
        return True
    else:
        return False

original_str = input("Enter a string: ")

if is_palindrome(original_str) == True:
    print(f''' "{original_str}" is a palindrome.''')
else:
    print(f''' "{original_str}" is not a palindrome.''')