n = int(input("Enter the length of the sequence: "))

n1 = 1
n2 = 2
count = 0

if n == 1:
   print(n1)
else:
   print("Fibonacci sequence upto",n,":")
   while count < n:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1