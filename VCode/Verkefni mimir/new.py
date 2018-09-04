num_int = int(input("Input a number: "))   
max_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))
    max_int = max(max_int, num_int)
else:
    print("The maximum is", max_int) 