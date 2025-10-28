print("Program starting.")

# Erotin CSV-tiedostossa
DELIMITER = ";"

# Viikonpäivät
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

try:
    # Kysytään käyttäjältä tiedoston nimi
    filename = input("Insert filename: ")

    print(f'Reading file "{filename}".')

    # Alustetaan apulistat viikonpäivien kulutuksia varten
    weekday_consumption = {day: 0.0 for day in WEEKDAYS}  # kWh
    weekday_total = {day: 0.0 for day in WEEKDAYS}        # €

    # Avataan tiedosto
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

        # Ohitetaan otsikkorivi ja käydään rivit läpi
        for i, line in enumerate(lines):
            if i == 0:
                continue  # Skipataan header

            row = line.strip()
            if row == "":
                continue  # Ohita tyhjät rivit

            # Jaetaan tiedot sarakkeisiin
            parts = row.split(DELIMITER)
            weekday = parts[0]
            consumption = float(parts[2])
            price = float(parts[3])

            total = consumption * price

            # Lisätään kulutukset sanakirjoihin
            if weekday in WEEKDAYS:
                weekday_consumption[weekday] += consumption
                weekday_total[weekday] += total

    # Tulostetaan viikonpäivittäin
    print("Analysing timestamps.")
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for day in WEEKDAYS:
        print(f" - {day}: total consumption {weekday_consumption[day]:.2f} kWh, total cost {weekday_total[day]:.2f} €")

except FileNotFoundError:
    print(f'Error: File "{filename}" not found.')
except Exception as e:
    print(f"An error occurred: {e}")
print("### Electricity consumption summary ###")
print("Program ending.")
