number = input("number: ")
number = float(number)
divisor = 1

sum_of_divisor = 0
while divisor < number:
    if number % divisor == 0 :
        sum_of_divisor = sum_of_divisor + divisor
    divisor = divisor + 1
