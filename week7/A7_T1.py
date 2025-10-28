# Ohjelma: Positiivisten kokonaislukujen kerääjä
print("Program starting.")
print("Collect positive integers.")

# Lista tallentamaan syötetyt luvut
numbers: list[int] = []

# Keräysvaihe
while True:
    try:
        value = int(input("Insert positive integer (negative stops): "))
        if value < 0:
            # Negatiivinen luku lopettaa keräyksen
            print("Stopped collecting positive integers.")
            break
        elif value == 0:
            # Nolla ei ole positiivinen eikä negatiivinen
            print("Zero is not positive, not collected.")
        else:
            # Positiivinen luku tallennetaan listaan
            numbers.append(value)
    except ValueError:
        # Jos käyttäjä ei syötä kokonaislukua
        print("Invalid input! Please insert an integer.")

# Tulostusvaihe
if len(numbers) == 0:
    print("No integers to display.")
else:
    print(f"Displaying {len(numbers)} integers:")
    for index, num in enumerate(numbers):
        ordinal = index + 1  # järjestysluku (1, 2, 3, ...)
        print(f"- Index {index} => Ordinal {ordinal} => Integer {num}")

print("Program ending.")
