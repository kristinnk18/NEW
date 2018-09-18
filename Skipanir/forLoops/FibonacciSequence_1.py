
n = int(input("Enter the length of the sequence: "))

a= [1,2,3]

for i in range(n-3):
    sum=0
    for j in a[-3:]:
        sum+=j
    a.append(sum)
print(a)