# Given a string named s, move the first 3 letters to the back of the string.
# Print it.
 
# For example, given s = "magic tortoise"
# the output will be
# ic tortoisemag

s = input("Input a string: ")

s_new = s[3:]                   # "ic tortoise"
s_new_2 = s_new + s[:3]         # "ic toroise + mag"
s = s_new_2                     # s = s_new_2

print(s)