# Assume an input string s of any length where all letters are lowercase.
 
# Write code which prints the index location of each letter 'o' in the string, one location per line of output.
# Hint: enumerate() is your friend!
 
# Given the string s = 'happiness is when what you think, what you say, and what you do are in harmony. - gandhi'
# the output will be:
# 24
# 40
# 58
# 62
# 75


s = input("Input a string: ")

target = "o"                        # finna hvar "o" er i setningu

for index, letter in enumerate(s):  #index list (s)
    if letter == target: 
        print(index)

# önnur útgáfa af sömu niðurstöðu._______________________________

s = input("Input a string: ")


for index, letter in enumerate(s):
    if letter == "o": 
        print(index)
