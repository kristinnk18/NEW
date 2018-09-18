
# Exercise no. 44 in chapter 4 in the textbook.
# You should output the result in a table, formatted in the following manner:
# The first line contains the word "Upper case", right justified, 15 spaces wide, followed by the Upper_count of upper case characters, right justified, 5 spaces wide.
# The second line contains the word "Lower case", right justified, 15 spaces wide, followed by the Upper_count of lower_count case characters, right justified, 5 spaces wide.
# The third line contains the word "Digits", right justified, 15 spaces wide, followed by the Upper_count of digits, right justified, 5 spaces wide.
# The fourth line contains the word "Punctuation", right justified, 15 spaces wide, followed by the Upper_count of punct characters, right justified, 5 spaces wide.
# The input prompt should be: "Enter a sentence. "
# Example input/output:


# # Enter a sentence: His name was John, lived at 47 Main Street, and was only 23 years old.
# #      Upper case     4
# #      Lower case    45
# #          Digits     4
# #     Punctuation     3

sentence = input("Enter a sentence: ")

Upper_count = 0
digit_count = 0
lower_count = 0
punctuation_count = 0
punct = '''!()-[]{};:'",<>\./?@#$%^&*_~'''

for i in sentence:
    if i.isupper():
        Upper_count += 1
    if i.isdigit():
        digit_count +=1
    if i.islower():
        lower_count += 1
    if i in punct:
        punctuation_count += 1



print("{:>15}{:>6}" .format("Upper case",Upper_count),"\n{:>15}{:>6}" .format("Lower case",lower_count), "\n{:>15}{:>6}" .format("Digits",digit_count),"\n{:>15}{:>6}" .format("Punctuation",punctuation_count))

            # {:<15} left alligned 15 bil
            # {:15}  right alligned 15 bbil
            
