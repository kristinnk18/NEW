def f():
    pass   # Skippar þessari línu.

def ping():
    return "ping!"

x = ping()

print(x)    # Prentar "ping!"

#############################################################
import math

def volume(r):              # volume er 'function'
    """returns the volume of spther with radius"""
    v = (4.0/3.0) * math.pi * r**3
    
    print("the value is: ") 
    return v

volume(2)


##############################################################


def example():
    print("bla")
    z = 3+9
    print(z)


example()    # Nauðsynlegt til að keyra forritið,, an "example()" gerist ekkert


###############################################################

input_1 = int(input("input number 1: "))
input_2 = int(input("input number 2: "))

def simple_answer (num1,num2):
    answer = num1 + num2
    print("num1 is",num1)
    print(answer)

simple_answer(input_1,input_2)     # setur 5 og 3 inni def

#  Þetta prentar :
#  num1 is 5
#  8
################################################################