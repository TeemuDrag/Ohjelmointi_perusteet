
print("Program starting")
def main():
    num= 0
    while True:
        print("Options")
        print("1 - Show count")
        print("2 - Increase count")
        print("3 - Reset count")
        print("0 - Exit")
        
        choice = input("Your choice: ")
        
        if choice == "1":
            print(f'Current count - {num}')
    
        elif choice == "":
            print("Exiting program.")
            break
        else:
            print("Unknown option! try again.")
    print("\nProgram ending.")
if __name__ == "__main__":
    main()
