
stop = "."
vowels = 'eaiou'

while True:
    word = input ("Enter a word: ")
    is_letter = ""
    if word == stop:
        break

    if word[0] in vowels:
        word = word + "yay"

    else:
        
        first_letter = ""
        second_letter = ""

        for letter in word:

            if letter in vowels:
                is_letter = True
            if is_letter:
                first_letter = first_letter + letter
            else:
                second_letter = second_letter + letter
        word = first_letter + second_letter + "ay"

        

    print(word)