# Write a function that takes a list L of integers as an argument and uses list comprehension to return
# the sum of the even integers in the list L.
 
# Hint: In your implementation, you can use some of the list functions discussed on page 349 in the textbook.
 
# The main program and one function is given - DO NOT change it.
 
# Example run:

# Enter elements of list separated by commas: 1,2,3,4,5,6,7,8,9
# 20


def even_sum(a_list):
    a_list = [int(x) for x in a_list]
    b_list = [i for i in a_list if i % 2 == 0]
    b_list = sum(b_list)
    return b_list

    

def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list


# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))


# def even_sum(a_list):
#     a_list = [int(x) for x in a_list]
#     b_list=[]
#     for i in a_list:
#         if i % 2 == 0:
#             b_list.append(i)
#     b_list = sum(b_list)
#     return b_list                    ##SAMA og squere
