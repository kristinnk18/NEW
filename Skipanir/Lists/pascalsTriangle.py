def make_new_row(x):
    new_list = []
    if x == []:
        return [1]
    elif x == [1]:
        return [1,1]

    new_list.append(1)
    for i in range(len(x)-1):
        new_list.append(x[i]+x[i+1])
    new_list.append(1)
    return new_list

# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
