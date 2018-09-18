# The Fibonacci sequence is: 1, 1, 2, 3, 5, 8, 13, ...

# Write a function, fibo, to print the first N numbers of the Fibonacci sequence.  There should be one space between the elements.

# Also write a statement to call fibo.

# n = int(input("Enter the length of the sequence: "))

# n1 = 1
# n2 = 2
# count = 0

# if n == 1:
#    print(n1)
# else:
#    print("Fibonacci sequence upto",n,":")
#    while count < n:
#        print(n1,end=' , ')
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1



def fibunacci(num):
  a,b = 1, 1
  for i in range(0, num):
    yield (a)
    a, b = b, a + b

n = int(input("Input the length of Fibonacci sequence (n>=1): "))

for item in fibunacci(n):
    print (item)