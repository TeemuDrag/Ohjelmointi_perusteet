print("Program starting.")

# Erotin CSV-tiedostossa
DELIMITER = ";"

try:
    # Kysytään käyttäjältä tiedoston nimi
    filename = input("Insert filename: ")

    print(f'Reading file "{filename}".')
    print("Electricity usage:")

    # Avataan tiedosto
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

        # Ohitetaan otsikkorivi
        for i, line in enumerate(lines):
            if i == 0:
                continue  # Skipataan header

            # Poistetaan rivinvaihto
            row = line.strip()
            if row == "":
                continue  # Ohita tyhjät rivit

            # Jaetaan tiedot sarakkeisiin
            parts = row.split(DELIMITER)
            weekday = parts[0]         # esim. Monday
            hour = parts[1]            # esim. 00:00
            consumption = float(parts[2])  # esim. 154.0
            price = float(parts[3])        # esim. 0.09

            # Lasketaan kokonaiskulutuksen hinta
            total = consumption * price

            # Tulostetaan tulos
            print(f" - {weekday} {hour}:00, price {price:.2f}, consumption {consumption:.2f} kWh, total {total:.2f} €")

except FileNotFoundError:
    print(f'Error: File "{filename}" not found.')
except Exception as e:
    print(f"An error occurred: {e}")

print("Program ending.")
