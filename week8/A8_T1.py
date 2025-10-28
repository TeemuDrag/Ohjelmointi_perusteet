import time

print("Program starting.")

def main():
    times = 0.0  # viiveen pituus sekunneissa
    
    while True:
        print("\nOptions")
        print("1 - Set pause duration")
        print("2 - Activate pause")
        print("0 - Exit")
        
        choice = input("Your choice: ").strip()
        
        if choice == "1":
            try:
                times = float(input("Insert pause duration (s): "))
                print(f"Pause duration set to {times} seconds.")
            except ValueError:
                print("Invalid number! Please insert numeric value.")
        
        elif choice == "2":
            print(f"Pausing for {times} seconds...")
            time.sleep(times)
            print("Unpaused.")
        
        elif choice == "0":
            print("Exiting program.")
            break
        
        else:
            print("Unknown option!")
    
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
