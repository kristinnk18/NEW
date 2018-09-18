# (In golf, pars for a hole range from 3 to 5.  
# Write a program using a while statement that allows the user to input the par and the score for each of the 18 holes.  
# Based on the number of shots compared to par, the program writes out the following:
#"invalid score", for less than 3 under par
#"albatross", for 3 under par
#"eagle", for 2 under par
#"birdie", for 1 under par
#"bogey", for 1 over par
#"double bogey", for 2 over par
#"triple bogey", for 3 over par
#"bad hole", for scores more than 3 over par
#The input/output should look like this:
#Par of hole 1: 5
#Score on hole 1: 6
#bogey
#Par of hole 2: 4
#Score on hole 2: 4
#par
#Par of hole 3: 3
#Score on hole 3: 5
#double bogey
#Par of hole 4: 4
#Score on hole 4: 3
#birdie
#etc.)

holeNum = 1

while holeNum <= 18:
    par = int(input("Par of hole " + str(holeNum) + ": "))
    score = int(input("Score on hole " + str(holeNum) + ": "))
    dif = score-par
    if dif < -3:
        print("invalid score")
    elif dif == -3:
        print ("albatross")
    elif dif == -2:
        print("eagle")
    elif dif == -1:
        print("birdie")
    elif dif == 0:
        print("par")
    elif dif == 1:
        print("bogey")
    elif dif == 2:
        print("double bogey")
    elif dif == 3:
        print("triple bogey")
    elif dif == 4:
        print("bad hole")
    holeNum += 1