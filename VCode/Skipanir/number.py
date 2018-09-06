
number = int(input("input a number: "))

max_number = number

while number > 0:
    if number > max_number:
        max_number = number

    number = int(input("input a number: "))

print(max_number)

# prentar ut stærstu töluna sem er innsleginn þangað til talan verður < 0.