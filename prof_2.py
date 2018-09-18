# Skrifið Python forrit sem les inn eina jákvæða heiltölu, n, 
# frá notanda og skrifar síðan út aðra hverja heiltölu frá n niður í 1, eina í hverri línu. 
# Inntak/úttak forritsins á að vera nákvæmlega eins og fram kemur í dæminu hér fyrir neðan.

# Write a Python program which reads a single positive integer, n, 
# from the user and then writes out every other integer from n down to 1, 
# each integer on a separate line.  
# The input/output of the program should be exactly the same as shown in the example below.

# Input an integer: 10
# 10
# 8
# 6
# 4
# 2



n = int(input("input an integer: "))



while n > 0:
    print(n)
    n = n - 2