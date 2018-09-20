with open('words.txt', 'r') as f:
    print(f, end="")
f.close()

line = ''
length = len(f)
last_sentence = 0
for i in range(0,length):
    m = f[i]
    if m in '.':
        line += f[last_sentence:i+1]
        line = line.strip().replace("\n", " ").replace(". ", ".")
        last_sentence = i+1
        text_file = open("sentences.txt", "w")
        text_file.write(line)
        text_file.close()
        
with open('sentences.txt', 'r') as f:
    data = f.read()
    print(data)