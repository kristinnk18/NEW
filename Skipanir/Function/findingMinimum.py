# # Write a function named find_min that takes two numbers as arguments and returns the minimum of the two.
# # Also write a statement that calls the function using the given input as arguments.

# Enter first number: 4
# Enter second number: 2
# Minimum:  2

# find_min function definition goes here

def find_min(first,second):
    return min(first,second)

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
minimum = find_min(first,second)

print("Minimum: ", minimum)
