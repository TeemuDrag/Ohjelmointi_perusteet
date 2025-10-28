from calculator_lib import add, subtract, multiply, divide

def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isdigit():
        return int(choice)
    return -1

def askValue(PPrompt: str) -> float:
    while True:
        try:
            value = float(input(PPrompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice in (1, 2, 3, 4):
            x = askValue("Insert first value: ")
            y = askValue("Insert second value: ")

            if choice == 1:
                result = add(x, y)
                print(f"{x} + {y} = {result}\n")
            elif choice == 2:
                result = subtract(x, y)
                print(f"{x} - {y} = {result}\n")
            elif choice == 3:
                result = multiply(x, y)
                print(f"{x} * {y} = {result}\n")
            elif choice == 4:
                if y == 0:
                    print("Error: Division by zero!\n")
                else:
                    result = divide(x, y)
                    print(f"{x} / {y} = {result}\n")
        else:
            print("Unknown option!\n")
    print("Program ending.")

if __name__ == "__main__":
    main()
