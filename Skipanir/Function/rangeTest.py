#  Write a function that takes an integer as an argument and returns True if the number
#  is within the range 1 to 555 (not inclusive, i.e. neither 1 nor 555 are in range).

# Also write a statement that calls the function with the given input as an argument.
 
# Example input/output:

# Enter a number: 1
# 1 is outside the range!

# The function definition goes here

def num_in_range(num):
    if num < 555 and num > 1:
        return True

    else:
        return False

num = int(input("Enter a number: "))

if num_in_range(num) == False:
    print(num, "is outside the range!")
else:
    print(num, "is in range.")



# You call the function here