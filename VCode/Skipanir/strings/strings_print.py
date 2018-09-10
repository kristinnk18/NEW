
message = "Hello world"

print(len(message)) # prentar út lengd orðsins: 11

print(message[2])   # prentar staf númer 3 "l" (0,1,2) í orðinu hello world: l

print(message[:3]) # prentar stafi 0 - 3: "hel"

print(message[6:])  # prentar "world"

# ".upper" er dæmi um method, segir til um hvernig einhvað er prentað út.

print(message.upper()) # Prentar allt í hástöfum "HELLO WORLD"

print(message.count("Hello")) # telur hversu oft "Hello" kemur fyrir: "1"

print(message.find("o"))  # finnur hvar "o" er i orðinu "hello world": "4"

new_message = message.replace("world", "skitur") # Replace-ar orðinu "world" fyrir "kiddi": "hello skitur"

print(new_message)  # prentar "hello kiddi"

greating = "hello"

name = "kiddi"

gr_name = "{}, {}. Godan dag".format(greating, name) # prentar "hello, kiddi. Godan dag"

print(gr_name) # prentar (gr_name)


#_____________________________________________________________________________________________________



a_str = "spam"
new_str = a_str[:1] + 'l' + a_str[2:] ###---1

print(a_str)    # Prentar "spam"
print(new_str)  # Prentar "slam" ###---1


# "len" er function sem breytir str i int í prentun.

how_many = len(a_str)
print(how_many)        # Prentar hversu margir stafir eru í a_str: "4"


print("Sorry, is this the {} minute {}?".format(5, 'ARGUMENT')) 
    #Prentar " Sorry, is this the 5 minute ARGUMENT?"

for i in range(5):
    print("{:10d} --> {:4d}" .format(i,i**2))   
    
        #  0  -->   0
        #  1  -->   1
        #  2  -->   4
        #  3  -->   9
        #  4  -->   16


#________________________________________________________________________________________________________


name = "Kristinn Örn Kristinsson"
first, middle, last = name.split() # splittar upp nafninu minu
transformed = last + ", " + first + " " + middle

print(middle)           # prentar "Örn"
print(transformed)      # Prentar "Kristinsson, Kristinn Örn"   


print("hello"[::-1])  # Prentar "hello" backwards. : "olleh"


#__________________________________________________________________________________________________________

for i in sentence:
    if i.isupper():             #upper case letter
        Upper_count += 1
    if i.isdigit():             # tölustafir
        digit_count +=1
    if i.islower():             #lower case letter
        lower_count += 1
    if i in punct:              #kommur og aukastafir:: punct = '''!()-[]{};:'",<>\./?@#$%^&*_~'''
        punctuation_count += 1





