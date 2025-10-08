print("Program starting.")

n = int(input("Insert a positive integer: "))

if n > 0:
    steps = 0
    print(n, end="")

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(f" -> {n}", end="")
        steps += 1

    print(f"\nSequence had {steps} total steps.")
else:
    print("Please insert a positive integer next time.")

print("\nProgram ending.")
