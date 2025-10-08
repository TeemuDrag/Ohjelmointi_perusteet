print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
r_num = int(input("Insert inspection point: "))

numbers = list(range(start, stop + 1))
if start <= r_num <= stop:
    print("\nFirst loop - inspection with break:")
    i = 0  
    while i < len(numbers):
        if numbers[i] == r_num:
            break
        print(numbers[i], end=" ")
        i += 1

    print("\nSecond loop - inspection with continue:")
    i = 0
    while i < len(numbers):
        if numbers[i] == r_num:
            i += 1
            continue
        print(numbers[i], end=" ")
        i += 1
else:
    print("\nInspection value must be within the range of start and stop.")

print("\n\nProgram ending.")
