

example = list()
example = []

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)

popped = primes.pop()

print(popped)
print(primes)

#######################################################################


courses = ["historym ", "math", "physics"]
courses_2 = ["art", "education"]

courses.append("art")                       #['historym ', 'math', 'physics', 'art']....bætir við art aftast

courses.insert(0, "art")                    #['art', 'historym ', 'math', 'physics', 'art']...bætir við art fremst [0]

courses.insert(0, courses_2)                # BÆTIR VIÐ COURSES_2 FREMST I COURSES LISTANN

# courses.sort()                              # RAÐAR LISTANUM Í STAFRÓFSRÖÐ
# courses.sort(reverse=True)                  # RAÐAR I ÖFUGA STAFROFSRÖÐ



print(courses[0])                           # PRENTAR ['art', 'education']

courses.extend(courses_2)                   # sama og .append - færir fyrir aftan i listann

print(courses.index("art"))                 # FINNUR NUMER HVAÐ ART ER I LISTANUM = "1"

print("art" in courses)                     # Skilar True ef art er i listanum


for word in courses:
    print(word)                             # prentar ut öll orðinn i courses lisatnum hvert og eitt

for index, word in enumerate(courses):
    print(index,word)                       # prentar út numer hvað orðið er i listanum og orðið " 0 Art" öll orðin.

##################################################################

kiddalist = list("Kiddi hvað ertu að gera")  #['K', 'i', 'd', 'd', 'i', ' ', 'h', 'v', 'a', 'ð', ' ', 'e', 'r', 't', 'u', ' ', 'a', 'ð', ' ', 'g', 'e', 'r', 'a']
print(kiddalist)                             #['K', 'i', 'd', 'd', 'i', ' ', 'h', 'v', 'a', 'ð', ' ', 'e', 'r', 't', 'u', ' ', 'a', 'ð', ' ', 'g', 'e', 'r', 'a']

for letter in kiddalist:                     # Prentar út " K i d d i   h v a ð   e r t u   a ð   g e r a "
    print(letter, end=" ")

# min()
# max()
# sum()


###################################################################

a_list = [3, 4, 5] + [6]
b_list = [3, 9]*2
result_list = []

for i, value in enumerate(a_list):
   value_to_append = value
   if b_list[i] > value:
       value_to_append = b_list[i]
   result_list.append(value_to_append)

print(result_list)

#############################################################

movies = ["Star Wars", "Ghandi", "Casablanca", "Bangsimon"]

gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)
print(gmovies)

###############################################################


squere = []
for i in range(1, 101):
    squere.append(i**2)                     ##SAMA og squere2

print(squere)

###################################################List Comprehension##################################################################

squere2 = [i**2 for i in range(1, 101)]
print(squere2)                              ##SAMA og squere

##########################

#movies er ofar i glosum..

movies = ["Star Wars", "Ghandi", "Casablanca", "Bangsimon"]
gmovies = [title for title in movies if title.startswith("G")]

print(gmovies)

#########################

v = [2, -3, 1]
w = [4*x for x in v]   #margfalda 4 við öll stök i v
print(w)

########################

# Carteisian products

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

carteisian_product = [(a, b)for a in A for b in B]

print(carteisian_product)  #[(1, 2), (1, 4), (1, 6), (1, 8), (3, 2), (3, 4), (3, 6), (3, 8), (5, 2), (5, 4), (5, 6), (5, 8), (7, 2), (7, 4), (7, 6), (7, 8)]

##########################

