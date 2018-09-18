# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
#  Write a function named is_prime that takes an integer argument and returns True if the number is prime 
# and False otherwise. 
# (Assume that the argument is an integer greater than 1, i.e. no need to check for erroneous input.)

# Also write code that calls the function and prints out a message saying that the given number 
# is a prime or not.

# Example input/output:

# Input an integer greater than 1: 7
# 7 is a prime

# Input an integer greater than 1: 6
# 6 is not a prime



# is_prime function definition goes here

# def prime_number(num):
#     if num % 2 == 0 or num < 2:
#         prime = False
#     else:
#         prime = True
#     return prime

    
# num = int(input("Input an integer greater than 1: "))

# if prime_number(num) == False:
#     print(num, "is not a prime")
# else:
#     print(num, "is a prime")

# Call the function here and print out the appropriate message

def prime_number(num):
    if num == 2:
        return True
    for x in range(2,num):
        if(num % x==0):
            return False
        else:
            prime = True

num = int(input("Input an integer greater than 1: "))

if prime_number(num) == False:
    print(num, "is not a prime")
else:
    print(num, "is a prime")
