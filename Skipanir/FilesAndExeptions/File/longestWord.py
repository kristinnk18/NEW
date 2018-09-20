# # Write a Python program that reads a file named words.txt containing one word/token per line with an empty line between sentences.  
# # The program prints out the longest word found in the file along with its length.

# Example output:
# Longest word is 'innflutningstollum' of length 18

with open("words.txt", "r") as words_txt:
    long = ""
    for word in words_txt:
        if len(word) > len(long):
            long = word.strip("\n")

    print("Longest word is '{}' of length {}".format(long, len(long))) ####### utgafa 1

    print(f"Longest word is '{long}' of length {len(long)}")           ####### utgafa 2

    # Longest word is 'innflutningstollum' of length 18