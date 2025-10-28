
print("Program starting.")
print("This program can read a file.")

# Ask user for the filename
filename = input("Insert filename: ")

try:
    # Open and read the file
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    # Print decorative start line
    print(f'#### START "{filename}" ####')
    print(content, end="")  # use end="" to avoid extra blank line
    print(f'\n#### END "{filename}" ####')

except FileNotFoundError:
    print(f'Error: File "{filename}" not found.')
except Exception as e:
    print(f"An error occurred: {e}")

print("Program ending.")
