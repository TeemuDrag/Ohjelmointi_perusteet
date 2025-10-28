# Ohjelma: Aikaleima-analyysi
# Tehtävä: Lukea .csv-tiedosto, analysoida rivit viikonpäivittäin ja näyttää tulokset.

# Vakio — viikonpäivien nimet
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    """Lukee tiedoston ja tallentaa rivit listaan PRows"""
    print(f'Reading file "{PFilename}".')

    # Tyhjennetään lista varmuuden vuoksi
    PRows.clear()

    try:
        # Avataan tiedosto lukutilassa
        with open(PFilename, "r", encoding="utf-8") as file:
            # Ohitetaan ensimmäinen rivi (otsikkorivi)
            header = file.readline()

            # Luetaan loput rivit yksi kerrallaan
            for line in file:
                # Poistetaan rivinvaihto ja ylimääräiset välilyönnit
                line = line.strip()
                # Jos rivi ei ole tyhjä, lisätään se listaan
                if line != "":
                    PRows.append(line)

    except FileNotFoundError:
        print(f'Error: File "{PFilename}" not found.')
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    """Laskee kuinka monta aikaleimaa löytyy kustakin viikonpäivästä"""
    print("Analysing timestamps.")

    # Tyhjennetään tuloslista
    PResults.clear()

    # Apulista viikonpäivien laskureille (alussa kaikki 0)
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]

    # Käydään kaikki rivit läpi
    for row in PRows:
        # Käydään kaikki viikonpäivät läpi ja tarkistetaan, alkaako rivi sillä
        for i, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                WeekdayTimestampAmount[i] += 1

    # Lisätään tulokset PResults-listaan tulostusta varten
    for i, day in enumerate(WEEKDAYS):
        PResults.append(f" - {day} {WeekdayTimestampAmount[i]} stamps")

    return None


def displayResults(PResults: list[str]) -> None:
    """Tulostaa analyysin tulokset käyttäjälle"""
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for result in PResults:
        print(result)
    print("### Timestamp analysis ###")
    return None


def main() -> None:
    """Ohjelman pääfunktio"""
    print("Program starting.")

    # Alustetaan tarvittavat listat
    rows: list[str] = []
    results: list[str] = []

    # Pyydetään käyttäjältä tiedoston nimi
    filename = input("Insert filename: ")

    # Luetaan tiedoston rivit
    readFile(filename, rows)

    # Analysoidaan rivit
    analyseTimestamps(rows, results)

    # Näytetään tulokset
    displayResults(results)

    # Tyhjennetään listat lopuksi
    rows.clear()
    results.clear()

    print("Program ending.")
    return None


# Käynnistetään ohjelma
main()
