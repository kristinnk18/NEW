
# Write a Python program using a for loop, tthat given two integers as input, prints the greatest common divisor (gcd) of them.
# GCD is the largest integer that divides each of the two integers.
# For example, given the numbers 12 and 15, the output will be:
# 3


m = int(input("Input the first integer: "))
n = int(input("Input the second integer: "))
gdb = 1

for i in range(1,m+1):
	if m%i == 0 and n%i == 0:
		gcd = i
print(gcd)