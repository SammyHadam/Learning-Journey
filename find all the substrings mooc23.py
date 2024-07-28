while True:
    word = input("Please type in a word: ")
    character = input("Please type in a character: ")
    index = word.find(character)
    if character in word:
        #output = word[index:]
        word1 = word[index:index+3]
        word2 = word[index:]
        #print(word[index:index+3])
        print(word1)
        print(word2)
        #if character in word2:
            
        #if len(output) >= 3:
          #print(output)