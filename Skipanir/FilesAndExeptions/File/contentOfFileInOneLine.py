# Write a program that reads a file called 'test.txt' and prints out the contents on the screen after removing all spaces and newlines. 
# Punctuations will be preserved.
 
# For example, if 'test.txt' contains:
# This is a test file, for chapter 06.
# This a new line in the file!
# Then, your program's output will show:
# Thisisatestfile,forchapter06.Thisanewlineinthefile!
# Hint:
# Consider using the strip() and replace() functions.


#################################################################

with open("test.txt", "r") as file_content:
    for word in file_content:
        print(word.replace(" ", "").strip("\n"), end="")

############################# Önnur Utgafa ########################

file_content = open("test.txt", "r")

for word in file_content:
    print(word.replace(" ", "").strip("\n"), end="")

file_content.close()