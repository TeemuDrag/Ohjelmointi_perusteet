print("Program starting.")
print("Testing decision structures.\n")

while True:
    # Käyttäjän syötteen kysyminen
    try:
        value = int(input("Insert an integer: "))
    except ValueError:
        print("Please insert a valid integer.\n")
        continue

    # Menu
    print("\nOptions:")
    print("1 - In one multi-branched decision")
    print("2 - Independent if-statement decisions")
    print("0 - Exit")
    choice = input("Your choice: ")

    # Moniharvainen päätös (if/elif/else)
    if choice == "1":
        print("Using one multi-branched decision structure.")
        result = value
        if value >= 400:
            result += 44
        elif value >= 200:
            result += 22
        elif value >= 100:
            result += 11
        print("Result is", result)

    # Itsenäiset if-lauseet
    elif choice == "2":
        print("Using multiple independent if-statements structure.")
        result = value
        if value >= 400:
            result += 44
        if value >= 200:
            result += 22
        if value >= 100:
            result += 11
        print("Result is", result)

    # Exit
    elif choice == "0":
        print("Exiting...")
        break

    # Tuntematon valinta
    else:
        print("Unknown option.")

    print("\n-------------------------------\n")

print("Program ending.")
