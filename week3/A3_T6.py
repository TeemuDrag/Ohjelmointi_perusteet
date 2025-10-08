print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")

# Päävalikko
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
main_choice = input("Your choice: ")

if main_choice == "1":
    # Length-valikko
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    length_choice = input("Your choice: ")
    
    if length_choice == "1":
        meters = float(input("Insert meters: "))
        km = meters / 1000
        print(f"{meters} m is {km} km")
    elif length_choice == "2":
        km = float(input("Insert kilometers: "))
        meters = km * 1000
        print(f"{km} km is {meters} m")
    elif length_choice == "0":
        print("Exiting length menu...")
    else:
        print("Unknown option.")

elif main_choice == "2":
    # Weight-valikko
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    weight_choice = input("Your choice: ")
    
    if weight_choice == "1":
        grams = float(input("Insert grams: "))
        pounds = grams * 0.002205  # 1 g ≈ 0.002205 lb
        print(f"{grams} g is {pounds:.4f} lb")
    elif weight_choice == "2":
        pounds = float(input("Insert pounds: "))
        grams = pounds / 0.002205
        print(f"{pounds} lb is {grams:.2f} g")
    elif weight_choice == "0":
        print("Exiting weight menu...")
    else:
        print("Unknown option.")

elif main_choice == "0":
    print("Exiting program...")
else:
    print("Unknown option.")

print("\nProgram ending.")
