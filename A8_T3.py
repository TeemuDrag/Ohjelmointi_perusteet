values = []

def showOptions() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")

def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isdigit():
        return int(choice)
    return -1

def openfile(filename):
    """Lukee tiedoston, muuntaa rivit liukuluvuiksi ja ohittaa tyhjät rivit."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            values.clear()  # Tyhjennetään vanhat arvot
            for line in file:
                line = line.strip()
                if line:  # Ohitetaan tyhjät rivit
                    try:
                        num = float(line)
                        values.append(num)
                    except ValueError:
                        print(f"Warning: '{line}' is not a number and was skipped.")
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')

def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.\n")
            break

        elif choice == 1:  # Lue tiedosto
            filename = input("Insert filename: ")
            openfile(filename)

        elif choice == 2:  # Näytä arvojen määrä
            print(f"Amount of values {len(values)}\n")

        elif choice == 3:  # Laske summa
            total = sum(values)
            print(f"Sum of values {round(total, 1)}\n")

        elif choice == 4:  # Laske keskiarvo
            if values:
                avg = sum(values) / len(values)
                print(f"Average of values {round(avg, 1)}\n")
            else:
                print("No values to calculate average.\n")

        else:
            print("Unknown option!\n")

    print("Program ending.")

if __name__ == "__main__":
    main()
