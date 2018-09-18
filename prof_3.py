# Skrifið Python forrit sem les inn tvær heiltölur frá notanda. 
# Fyrri talan stendur fyrir upphafsgildi á röð og seinni talan stendur fyrir mismun á sérhverjum 
# samliggjandi gildum raðarinnar. Forritið skrifar síðan út sérhvert 
# gildi raðarinnar (með einu bili á milli gilda) þangað til summa gildanna er orðin >= 100. 
# Í lokin skrifast jafnframt út summan.
# Inntak/úttak forritsins á að vera nákvæmlega eins og fram kemur í dæminu hér fyrir neðan.
 
# Write a Python program which reads two integers from the user. 
# The first integer denotes the initial value of a series and the second integer denotes the 
# difference between any two consecutive values in the series. The program then writes out 
# each value of the series (with one space between values) until the sum of the values is >= 100. 
# Finally, the sum is written out.

# The input/output of the program should be exactly the same as shown in the example below.

# Initial value: 1
# Step: 4
# 1 5 9 13 17 21 25 29
# Sum of series: 120

# Initial value: Step: 1 5 9 13 17 21 25 29 
# Sum of series: 120

# value = int(input("Initial value: "))
# step = int(input("Step: "))
# sum_of_series = 0
# list = []


# while sum_of_series <= 100:
#     list.append (value)
#     sum_of_series += value
#     value = value + step
# print((list), "Sum of series: ",(sum_of_series))

# print(n1,end=' , ')

value = int(input("Initial value: "))
step = int(input("Step: "))
sum_of_series = 0
list = []


while sum_of_series <= 100:
    sum_of_series += value
    print(value,end=" ")
    value = value + step
print("\nSum of series: ",(sum_of_series))








