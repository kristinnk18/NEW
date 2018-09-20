# Write a function named safe_input(prompt, type) that works like the Python input function, 
# except that it only accepts the specified type of input.  The function two arguments:
 
# prompt: of type string
# a_type: either the type int, float or str

# The function should keep prompting the user for input until the user inputs the correct type. 
#  At the end the function should return the converted value.

# Please enter an integer: Error: please enter a value of  <class 'int'>
# Please enter an integer: Error: please enter a value of  <class 'int'>
# Please enter an integer: 2
# Please enter a float: Error: please enter a value of  <class 'float'>
# Please enter a float: 23.3
# Please enter a string: 45


# Here is the definition of safe_input. It should contain this exception:

def safe_input(prompt, a_type):
    '''Here is the definition of safe_input. It should contain this exception'''
    while True:
        try:
            if a_type ==  int:
                value = int(input(prompt))
                break
            if a_type == float:
                value = float(input(prompt))
                break
            if a_type == str:
                value = str(input(prompt))
                break
            
        except ValueError:
            print("Error: please enter a value of ", a_type)
    

    return value

# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))