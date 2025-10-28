import timestamp_lib as ts

def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isdigit():
        return int(choice)
    return -1

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")

    timestamps = []
    ts.readTimestamps(filename, timestamps)

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.\n")
            break

        elif choice == 1:
            year_input = input("Insert year: ")
            if year_input.isdigit():
                amount = ts.calculateYears(int(year_input), timestamps)
                print(f"Amount of timestamps during year '{year_input}' is {amount}\n")
            else:
                print("Invalid year input.\n")

        elif choice == 2:
            month_input = input("Insert month: ")
            amount = ts.calculateMonths(month_input, timestamps)
            print(f"Amount of timestamps during month '{month_input}' is {amount}\n")

        elif choice == 3:
            weekday_input = input("Insert weekday: ")
            amount = ts.calculateWeekdays(weekday_input, timestamps)
            print(f"Amount of timestamps during weekday '{weekday_input}' is {amount}\n")

        else:
            print("Unknown option!\n")

    print("Program ending.")

if __name__ == "__main__":
    main()
