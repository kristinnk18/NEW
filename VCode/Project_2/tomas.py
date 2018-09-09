
while True:
    original = input ("Enter a word: ")
    word = original
    broken = ""

    if original == ".":
        break

    if word[0] in 'aeiou':
        ending = "yay"
        new_word = word + ending

    else:
        ending = "ay"

        first = ""
        second = ""

        for letter in word:
            if letter in 'aeiou':
                broken = True
            if broken:
                first += letter
            else:
                second += letter
        new_word = first + second + ending

    print(new_word)