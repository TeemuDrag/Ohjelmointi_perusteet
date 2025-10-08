print("Program starting.")
print("String comparisons")
w1=input("Insert first word: ")
char=input("Insert a character: ")
if char in w1:
    print("Word \"" + w1 + "\" contains character \""+char+"\"")

else:
    print("Word \"" + w1 + "\" doesn't contain character \""+char+"\"")


w2=input("Insert second word: ")
if w1 < w2:
    print(f'The first word "{w1}" is before the second word "{w2}" alphabetically.')
elif w2 < w1:
    print(f'The second word "{w2}" is before the first word "{w1}" alphabetically.')
else:
    print(f'Both inserted words are the same alphabetically, "{w1}"')

print("Program ending.")
