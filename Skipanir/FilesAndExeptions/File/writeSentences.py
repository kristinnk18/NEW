import random
import string


def get_word_string(filename):
    wordString = ""
    try:
        with open(filename, 'r') as f:
            word = f.read()
            word = word.split()
        return word
    except FileNotFoundError:
        print("File X not found")
    return wordString

def scramble_string(string):
    chars = []
    for word in string:
        new_word = []
        wordlist = list(word)
        first, mid, last = wordlist[0], wordlist[1:-1], wordlist[-1]
        random.shuffle(mid)
        new_word.append(first)
        for x in mid:
            new_word.append(x)
        new_word.append(last)
        new_word = ''.join(new_word)
        chars.append(new_word)

    sentence = " ".join(chars)
#         word_list = [['obytay'], ['ikeslay'], ['ishay'], ['artway']]
# >>> print ' '.join(word[0] for word in word_list)
# obytay ikeslay ishay artway

    return sentence



# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)