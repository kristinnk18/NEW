# https://github.com/kristinnk18/NEW

start = 1_1
notvalid = "Not a valid direction!"




while True:
    if start == 1_1:
        print("You can travel: (N)orth.")
        direction = input("Direction: ").lower()
        while direction != "n":
            print(notvalid)
            direction = input("Direction: ").lower()
        if direction == "n":
            start = 1_2

    if start == 1_2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = input("Direction: ").lower()
        while direction not in {"n","e","s"}:
            print(notvalid)
            direction = input("Direction: ").lower()
        if direction == "n":
            start = 1_3
        elif direction == "s":
            start = 1_1
        elif direction == "e":
            start = 2_2
        else:
            print(notvalid)
            start = 1_2

    if start == 1_3:
        print("You can travel: (E)ast or (S)outh.")
        direction = input("Direction: ").lower()
        while direction not in {"e","s"}:
            print(notvalid)
            direction = input("Direction: ").lower()
        if direction == "e":
            start = 2_3
        elif direction == "s":
            start = 1_2
        else:
            print(notvalid)
            start = 1_3

    if start == 2_1:
        print("You can travel: (N)orth.")
        direction = input("Direction: ").lower()
        while direction not in {"n"}:
            print(notvalid)
            direction = input("Direction: ").lower()
        if direction == "n":
            start = 2_2
        else:
            print(notvalid)
            start = 2_1

    if start == 2_2:
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ").lower()
        while direction not in {"w","s"}:
            print(notvalid)
            direction = input("Direction: ").lower()
        if direction == "w":
            start = 1_2
        elif direction == "s":
            start = 2_1
        else:
            print(notvalid)
            start = 2_2

    if start == 2_3:
        print("You can travel: (E)ast or (W)est.")
        direction = input("Direction: ").lower()
        while direction not in {"e","w"}:
            print(notvalid)
            direction = input("Direction: ").lower()
        if direction == "w":
            start = 1_3
        elif direction == "e":
            start = 3_3
        else:
            print(notvalid)
            start = 2_3

    if start == 3_1:
        print("Victory!")
        break

    if start == 3_2:
        print("You can travel: (N)orth or (S)outh.")
        direction = input("Direction: ").lower()
        while direction not in {"n","s"}:
            print(notvalid)
            direction = input("Direction: ").lower()
        if direction == "n":
            start = 3_3
        elif direction == "s":
            start = 3_1
        else:
            print(notvalid)
            start = 3_2

    if start == 3_3:
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ").lower()
        while direction not in {"w","s"}:
            print(notvalid)
            direction = input("Direction: ").lower()
        if direction == "s":
            start = 3_2
        elif direction == "w":
            start = 2_3
        else:
            print(notvalid)
            start = 3_3


    


    
    


    