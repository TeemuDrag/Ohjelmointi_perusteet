print("""Program starting. 
Estimate how many minutes you spent on programming...""")
print()

w=input("Insert a closed compound word: ")
käännetty = w[::-1]
viimeinen = w[-1]
print("The word you inserted is '"+w+"' and in reverse it is '"+käännetty+"'.")
print("The inserted word length is "+str(len(w)))
print("Last character is '"+viimeinen+"'")
print()

print("Take substring from the inserted word by inserting...")
sp=int(input("1) Starting point: "))
ep=int(input("2) Ending point: "))
ss=int(input("3) Step size: "))
substring = w[sp:ep:ss]
print()
print("The word '"+w+"' sliced to the defined substring is '"+substring+"'.")


print()
print("Program ending.")
