nested = []
nested2 = []
nested.append(nested2)
words = []
false = False
while false == False:
    word_input = input()
    if word_input != "s":
        words.append(word_input)
        words.sort()
    else:
        break
print(words)