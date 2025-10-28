from dataclasses import dataclass

DELIMITER = ";"

@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

def readTimestamps(filename: str, timestamps: list[TIMESTAMP]) -> None:
    """Lukee CSV-tiedoston ja täyttää annetun listan TIMESTAMP-objekteilla"""
    timestamps.clear()  # tyhjennetään lista varmuuden vuoksi
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:
                    continue  # ohitetaan otsikko
                line = line.strip()
                if not line:
                    continue
                parts = line.split(DELIMITER)
                ts = TIMESTAMP(
                    weekday=parts[0],
                    hour=parts[1],
                    consumption=float(parts[2]),
                    price=float(parts[3])
                )
                timestamps.append(ts)
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def displayTimestamps(timestamps: list[TIMESTAMP]) -> None:
    """Näyttää jokaisen aikaleiman ja laskee kokonaiskulutuksen"""
    print("Electricity usage:")
    for ts in timestamps:
        total = ts.consumption * ts.price
        print(f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, consumption {ts.consumption:.2f} kWh, total {total:.2f} €")

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps: list[TIMESTAMP] = []
    readTimestamps(filename, timestamps)
    if timestamps:
        displayTimestamps(timestamps)
    print("Program ending.")

if __name__ == "__main__":
    main()
