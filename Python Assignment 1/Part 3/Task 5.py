def backwardString(sentence):
    words = sentence.split()
    result = []
    for word in words:
        result.insert(0, word)
    return " ".join(result)

sentence = input("Enter a sentence: ")
print(backwardString(sentence))