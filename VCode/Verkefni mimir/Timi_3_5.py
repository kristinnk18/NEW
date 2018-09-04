n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
count = 2
prime = True

while count < n:
    if n % count == 0:
        prime = False
    count += 1
# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("!Prime")