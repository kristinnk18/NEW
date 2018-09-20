# file_content = open("test.txt", "r", encoding="utf-8")

# for word in file_content:
#     print(word,end="")

# file_content.close()

###############################################################

with open("test.txt", "w") as file_content:
    print("Kiddi", file=file_content)


###############################################################