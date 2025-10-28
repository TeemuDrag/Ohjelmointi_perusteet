print("Program starting.")
print("This program analyses a list of names from a file.")

# Pyydetään käyttäjältä tiedoston nimi
filename = input("Insert filename to read: ")

try:
    # Avataan tiedosto lukutilassa (r = read)
    # encoding="utf-8" varmistaa, että ääkköset toimivat oikein
    with open(filename, "r", encoding="utf-8") as file:
        names = []  # lista, johon tallennetaan nimet

        # Luetaan tiedosto rivi kerrallaan
        for line in file:
            # Poistetaan rivinvaihdot ja ylimääräiset välilyönnit
            name = line.strip()
            # Lisätään nimi listaan, jos rivi ei ole tyhjä
            if name:
                names.append(name)

    # Muutetaan lista yhdeksi merkkijonoksi, nimet erotettuna puolipisteellä
    names_string = ";".join(names)

    # Lasketaan nimiin liittyviä tietoja
    name_lengths = [len(name) for name in names]  # pituudet
    name_count = len(names)                       # nimien määrä
    shortest = min(name_lengths)                  # lyhin nimi
    longest = max(name_lengths)                   # pisin nimi
    average = sum(name_lengths) / name_count if name_count > 0 else 0  # keskipituus

    # Luodaan raportti muotoiltuna merkkijonona (kaksi desimaalia)
    report = (
        f"Name count - {name_count}\n"
        f"Shortest name - {shortest} chars\n"
        f"Longest name - {longest} chars\n"
        f"Average name - {average:.2f} chars"
    )

    # Tulostetaan raportti
    print("Analysing names...")
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(report)
    print("#### REPORT END ####")

# Jos tiedostoa ei löydy
except FileNotFoundError:
    print(f'Error: File "{filename}" not found.')

# Jos tapahtuu jokin muu virhe
except Exception as e:
    print(f"An error occurred: {e}")

print("Program ending.")
