#  Write a function named count_case that takes a string as an argument and returns the count
#  of upper case and lower case characters in the string (in that order). 
 
# Also write a statement that calls the function with the given input as an argument.
 
# Example input/output:

# Enter a string: However, Marie found the best solution.
# Upper case count:  2
# Lower case count:  30



# Your function definition goes here

def count_case(user_input):
    lower = sum(1 for i in user_input if i.islower())
    upper = sum(1 for i in user_input if i.isupper())
    return upper, lower

user_input = input("Enter a string: ")

# Call the function here
upper, lower = count_case(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)