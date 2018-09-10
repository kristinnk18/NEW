# Write a Python program using for loops that, given an integer n, prints all the perfect top_nums from 1 to n.
# A perfect top_num is an integer whose sum of integer divisiors (excluding the top_num itself) add up to the top_num.
# For example, 6 is a perfect top_num because the sum of its integer divisors (1+2+3) is equal to 6.

top_num = int(input("Upper number for the range: ")) # Do not change this line

for number in range(2,top_num+1):
    sum_of_divisiors = 0
    for divisior in range(1, number):
        if number % divisior == 0:
            sum_of_divisiors += divisior
    if number == sum_of_divisiors:
        print(number)
