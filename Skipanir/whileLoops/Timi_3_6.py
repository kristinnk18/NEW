#Write a program using a while statement, that prints out the two-digit number such that when you square it, 
# the resulting three-digit number has its rightmost two digits the same as the original two-digit number.  
# That is, for a number in the form AB:
# AB * AB = CAB, for some C. 

count = 10 

while count <= 100:
    total = count * count
    if total % 100 == count:
        print(count)
        break
    count +=1