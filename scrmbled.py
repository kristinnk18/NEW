import random
random.seed(10)

# Open the file is input is not there create one
try:
    in_text = open("in.txt", "r")
    out_text = open("out.txt", "w")
except IOError:
    print("File in.txt does not exist creating default one.")
    in_file = open("in.txt", "w")

    string = """\
According to research at an English university, it doesn't matter in what order the letters in a word are, the only important thing is that the first and last letter is a the right place.
The rest can be a total mess and you can still read it without any problem.
This is because we do not read every letter by itself but the word as a whole.\
""".strip()

    print(string, file = in_file)
    in_file.close()
    in_text = open("in.txt", "r")
    out_text = open("out.txt", "w")

# Function to shuffle the chars around
def shuffle(word):
    if len(word) == 1:
        return word
    else:
        half = int(len(word) / 2)
        # First half in reverse
        first = word[:half][::-1]
        # Last half in reverse
        last = word[half:len(word)][::-1]

        # First + Last in reverse
        return str(first+last)[::-1]

# Function to scramble the word
def scramble(sentence):

    return ' '.join([word[0] + ''.join(random.sample([char for char in word[1:-1]],len(word[1:-1]))) + word[-1] if len(word) > 1 else word for word in  sentence.split()])

# Read the input and write the scrambled words to the output
for line in in_text:
    random.seed(10)
    line = line.strip()
    new_line = ""

    for word in line.split(" "):
        new_line += scramble(word) + " "

    print(new_line, file = out_text)

# Close open files
in_text.close()
out_text.close()