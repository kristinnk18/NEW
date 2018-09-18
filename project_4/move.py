
HIGHEST = 10
LOWEST = 1

def find_min(newinput, position):

    if newinput == "r":
        if position < HIGHEST:
            position +=1
        else:
            position = position
    elif newinput == "l":
        if position > LOWEST:
            position -=1
        else:
            position = position
    return(position)


position = int(input("Input a position between 1 and 10: "))

while True:

    newinput = input("l - for moving left\nr - for moving right\nAny other letter for quitting\nInput your choice: ")
    
    if newinput == "r" or newinput == "l":
        position = find_min(newinput, position)
        print("New position is:", position)
    else:
        print("New position is:", position)
        break
