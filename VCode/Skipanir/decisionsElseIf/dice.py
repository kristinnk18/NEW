d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

sum = int(d1 + d2)

if d1 <= 0 or d1 > 6 or d2 <= 0 or d2 > 6:
    print("Invalid input")
elif sum == 7 or sum == 11:
    print("Winner")
elif sum == 2 or sum == 3 or sum == 12:
    print("Loser")
else:
    print(sum)