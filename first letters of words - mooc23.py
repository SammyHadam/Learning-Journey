words = input("Please type in a sentence: ")
blank = ' '
print(words[0])

while len(words) >= len(blank):
    index = words.find(blank)
    if index != -1 and len(words) >= 0:
        output = words[index:]
        if output[1] != blank:
            print(output[1])
            words = words[index + 1:]
    else:
        break