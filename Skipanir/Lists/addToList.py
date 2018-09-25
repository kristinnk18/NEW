# Example input/output:
 
# Enter value to be added to list: a
# Enter value to be added to list: b
# Enter value to be added to list: c
# Enter value to be added to list: exit
# a
# b
# c
# a
# b
# c
# a
# b
# c

def populate_list(initial_list):
    while True:
        list_input = input("Enter value to be added to list: ")
        if list_input.upper() == "EXIT":
            break
        initial_list.append(list_input)
    return initial_list

def triple_list(initial_list):
    new_list = initial_list
    return new_list*3


initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
