# Given a string of any length, extract the numbers (digits) and print them on one line without spaces.
 
# Hint 1: start with an empty string
# Hint 2: isdigit() is your friend.
 
# For example, given this string:
# some 1! likes 2 put 14 digits, in 3 strings
# the output will be
# 12143


s = input("Input a string: ")


emty_string = " "

for digit in s:
    if digit.isdigit():                     #finnur hvort tala sé í inputinu.
        emty_string = emty_string + digit

print(emty_string)



