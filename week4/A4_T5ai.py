print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))


error = False

if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    error = True

if not (start <= inspection <= stop):
    print("Inspection value must be within the range of start and stop.")
    error = True

if not error:
    print("\nFirst loop - inspection with break:")
    first_output = []
    for i in range(start, stop + 1):
        if i == inspection:
            break
        first_output.append(str(i))
    print(" ".join(first_output))
    print("\nSecond loop - inspection with continue:")
    second_output = []
    for i in range(start, stop + 1):
        if i == inspection:
            continue
        second_output.append(str(i))
    print(" ".join(second_output))

print("\nProgram ending.")
