SEPARATOR = ";"


def readValues(filename: str) -> list:
    """Lukee tiedostosta numeeriset arvot ja palauttaa ne listana."""
    numbers = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                value = line.strip()
                if value:
                    try:
                        num = float(value)
                        numbers.append(num)
                    except ValueError:
                        print(f"Warning: '{value}' is not a number and was skipped.")
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    return numbers


def analyseValues(numbers: list) -> str:
    """Analysoi numerolistan ja palauttaa tuloksen CSV-muodossa otsikkorivin kanssa."""
    count = len(numbers)
    total = sum(numbers) if count > 0 else 0
    greatest = max(numbers) if count > 0 else 0
    average = total / count if count > 0 else 0

    # Luo raportti otsikolla ja tuloksilla
    header = "Count;Sum;Greatest;Average"
    data = f"{count}{SEPARATOR}{total:.0f}{SEPARATOR}{greatest:.0f}{SEPARATOR}{average:.2f}"
    return f"{header}\n{data}\n"


def main():
    """Pääohjelma, joka lukee tiedoston ja näyttää analyysin."""
    print("Program starting.")

    filename = input("Insert filename: ")

    numbers = readValues(filename)

    if numbers:  # jos lista ei ole tyhjä
        report = analyseValues(numbers)

        print("#### Number analysis - START ####")
        print(f'File "{filename}" results:')
        print(report, end="")  # end="" jotta ei lisätä ylimääräistä tyhjää riviä
        print("#### Number analysis - END ####")

    print("Program ending.")


if __name__ == "__main__":
    main()
