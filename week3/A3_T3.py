print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")

name = input("Before the menu, please insert your name: ")
print()

print("""Options:
1 - Print welcome message
0 - Exit""")

choice = input("Your choice: ")

if choice == "1":
    print("Welcome " + name + "!")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print()
print("Program ending.")
