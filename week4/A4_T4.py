print("Program starting.\n")


words = []
while True:
    word = input("Insert word (empty stops): ")
    if word == "":       
        break
    words.append(word)

# Lasketaan sanat ja kirjaimet
num_words = len(words)
num_letters = sum(len(w) for w in words)
print("You inserted:")
print("-",num_words,"words")
print("-", num_letters,"characters")

print("\nProgram ending.")