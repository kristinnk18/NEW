# a = int(input("number :"))
# b = int(input("number :"))

# try:
#     c = a // b
#     print(c)

# except:
#     print("there was an errror")


###############################################

try:
    a = int(input("number :"))
    b = int(input("number :"))

except ValueError:
    print("there was an error")

try:
    c = a // b
    print(c)

except ZeroDivisionError as error:
    print(error)

except NameError as name_error:
    print(name_error)


#################################################
