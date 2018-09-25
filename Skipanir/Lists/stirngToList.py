# Write a function called 'to_list' that takes a string as a parameter and returns a list of words in the string.
# "Words" are entities that are seperated by either commas (',') or spaces (' '). 
# In case the string contains neither commas nor spaces, a list should be returned containing a single element.
# Note: We are not testing for the case where both commas and spaces are present in the string so feel free to ignore that.
# The main program is given - DO NOT change it.
# Example input/output:
# Enter the string: this is a string
# ['this', 'is', 'a', 'string']
 
# Enter the string: Pranshu,Enbody,Alireza
# ['Pranshu', 'Enbody', 'Alireza']



# import string
# # The main program starts here - DO NOT change it
# the_string = input("Enter the string: ")
# the_string = the_string.split()
# to_list_the_string = list(the_string)
# the_list = to_list_the_string
# # the_list = to_list(the_string)
# print(the_list)

def to_list(the_string):
    if "," in the_string:
        the_string = the_string.split(",")
    else:
        the_string = the_string.split()
    the_list = list(the_string)
    return the_list

# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)