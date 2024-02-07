from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter your word to Search: ")
    if word == "":
        break
    
    print(dictionary.meaning(word))
