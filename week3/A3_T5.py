print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice = input("Your choice: ")

if choice == "1":
    c = float(input("Insert the amount of Celsius: "))
    f = c * 9 / 5 + 32
    print(f"{c} °C equals to {f} °F")
elif choice == "2":
    f = float(input("Insert the amount of Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"{f} °F equals to {c} °C")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")
