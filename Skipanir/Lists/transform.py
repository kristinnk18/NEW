# Implement the transform function described in assignment 54 on page 417 in the textbook:
# It is often times advantageous to be able to transfer data between multiple lists while rearranging their order.
# For instance, say that list1 = [1,2,3,4,5,6,7,8,9] and you wish to add the numbers in the index range 4:7 of list1 to another list, 
# list2, in reverse order while simultaneously removing them from list1. 
# If list2 = [100,200], the result will be list2 = [100,200,7,6,5]. 
# Write a function named transform that takes as arguments list1, list2, r1, and r2,
# that removes items from list1 in the slice r1:r2, appends them onto list2 in reverse order,
# and returns the resulting list. For example, in this case, the function call will be tranform(list1, list2, 4, 7).

# The main program and two functions are given and you are NOT allowed to change this code.
 
# Example:
# if list1 = [1,2,3,4,5,6,7,8,9] and list2 = [100,200,300] and the range is 4:7
# then the result of calling the transform function is:
 
# list1 = ['1', '2', '3', '4', '8', '9']
# ['100', '200', '300', '7', '6', '5']


def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def get_integer(prompt):
    val = int(input(prompt))
    return val

def transform(list1, list2, index1, index2):
    list1.sort()
    list1_del = list1[index1:index2]
    del list1[index1:index2]
    list1_del.reverse()
    list2.sort()
    for x in list1_del:
        list2.append(x)

    return transform


# Main program starts here - DO NOT change it
list1 = get_list()
list2 = get_list()
index1 = get_integer("Enter from value: ")
index2 = get_integer("Enter to value: ")
transform(list1, list2, index1, index2)
print(list1)
print(list2)