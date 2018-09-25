# Write a program that makes a list of the unique letters in an input sentence.  
# That is, if the letter "x" is used twice in a sentence, it shouild only appear once in your list.  
# Neither punctuation nor white space should appear in your list.

import string

sentence = input("Input a sentence: ")
unique_letters = []
for x in sentence:
    if x.isalpha() and x not in unique_letters:
        unique_letters.append(x)

print("Unique letters:", unique_letters)

