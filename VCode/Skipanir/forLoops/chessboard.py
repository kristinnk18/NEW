# If a chessboard were to have wheat placed upon each square such that one grain were placed on the first square, 
# two on the second, four on the third, and so on (doubling the number of grains on each subsequent square), 
# how many grains of wheat would be on the chessboard at the finish?
# Write a Python program using a for loop that calculates and prints out this number of grains.

grains  = 0
for x in range(1, 65):
    grains += 2**(x - 1)
else:
    print(x, grains)
