north = "n"
south = "s"
west = "w"
east = "e"
end = 3_1
start = 1_1
notvalid = "Not a valid direction!"



while True:
    if start == 1_1:
        print("you can travel: (N)orth.")
        direction = input("direction: ")
        if direction == "n":
            start = 1_2
        else:
            print(notvalid)
            start = 1_1

    if start == 1_2:
        print("you can travel: (N)orth or (E)ast or (S)outh.")
        direction = input("direction: ")
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
        print("you can travel:(E)ast or (S)outh.")
        direction = input("direction: ")
        if direction == "e":
            start = 2_3
        elif direction == "s":
            start = 1_2
        else:
            print(notvalid)
            start = 1_3

    if start == 2_1:
        print("you can travel:(N)orth.")
        direction = input("direction: ")
        if direction == "n":
            start = 2_2
        else:
            print(notvalid)
            start = 2_1

    if start == 2_2:
        print("you can travel:(W)est or (S)outh.")
        direction = input("direction: ")
        if direction == "w":
            start = 1_2
        elif direction == "s":
            start = 2_1
        else:
            print(notvalid)
            start = 2_2

    if start == 2_3:
        print("you can travel:(W)est or (E)ast")
        direction = input("direction: ")
        if direction == "w":
            start = 1_3
        elif direction == "e":
            start = 3_3
        else:
            print(notvalid)
            start = 2_3

    if start == 3_1:
        print("Vctory!")
        break

    if start == 3_2:
        print("you can travel:(N)orth or (S)outh.")
        direction = input("direction: ")
        if direction == "n":
            start = 3_3
        elif direction == "s":
            start = 3_1
        else:
            print(notvalid)
            start = 3_2

    if start == 3_3:
        print("you can travel:(W)est or (S)outh.")
        direction = input("direction: ")
        if direction == "s":
            start = 3_2
        elif direction == "w":
            start = 2_3
        else:
            print(notvalid)
            start = 3_3


    


    
    


    