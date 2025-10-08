print("Program starting.\n")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

print("\nStarting for-loop:")
for i in range(start, stop + 1):   # +1 jotta loppuarvo tulee mukaan
    print(i)

print("\nProgram ending.")