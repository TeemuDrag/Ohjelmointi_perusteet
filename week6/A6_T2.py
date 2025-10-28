print("Program starting.")

# Kysytään tiedot
first_name = input("Insert first name: ")
last_name = input("Insert last name: ")
filename = input("Insert filename: ")

# Kirjoitetaan tiedosto
with open(filename, "w", encoding="utf-8") as file:
    file.write(f"{first_name}\n")
    file.write(f"{last_name}\n")
    file.write("\n")  # tyhjä rivi loppuun
    print("Program ending.")
    import sys
# Ohjelma päättyy luonnollisesti tässämom

