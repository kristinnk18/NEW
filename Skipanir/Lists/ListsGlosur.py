

example = list()
example = []

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)

popped = primes.pop()

print(popped)
print(primes)

######################################################


courses = ["historym ", "math", "physics"]
courses_2 = ["art", "education"]

courses.append("art")                       #['historym ', 'math', 'physics', 'art']....bætir við art aftast

courses.insert(0, "art")                    #['art', 'historym ', 'math', 'physics', 'art']...bætir við art fremst [0]

courses.insert(0, courses_2)                # BÆTIR VIÐ COURSES_2 FREMST I COURSES LISTANN

courses.sort()                              # RAÐAR LISTANUM Í STAFRÓFSRÖÐ
courses.sort(reverse=True)                  # RAÐAR I ÖFUGA STAFROFSRÖÐ



print(courses[0])                           # PRENTAR ['art', 'education']

courses.extend(courses_2)                   # sama og .append - færir fyrir aftan i listann

print(courses.index("art"))                 # FINNUR NUMER HVAÐ ART ER I LISTANUM = "1"

print("art" in courses)                     # Skilar True ef art er i listanum


for word in courses:
    print(word)                             # prentar ut öll orðinn i courses lisatnum hvert og eitt

for index, word in enumerate(courses):
    print(index,word)                       # prentar út numer hvað orðið er i listanum og orðið " 0 Art" öll orðin.


