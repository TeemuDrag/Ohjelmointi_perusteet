from dataclasses import dataclass

# Vakio
DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

# Tietorakenteet
@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

@dataclass
class DAY_USAGE:
    weekday: str
    total_consumption: float = 0.0
    total_cost: float = 0.0

def readTimestamps(filename: str, timestamps: list[TIMESTAMP]) -> None:
    """Lukee CSV-tiedoston ja täyttää TIMESTAMP-listan"""
    timestamps.clear()
    print(f'Reading file "{filename}".')
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
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

def analyseTimestamps(timestamps: list[TIMESTAMP], analysis: list[DAY_USAGE]) -> None:
    """Laskee päivittäisen kulutuksen ja kustannuksen"""
    analysis.clear()
    # Luo DAY_USAGE-objekti jokaiselle viikonpäivälle
    day_map = {day: DAY_USAGE(day) for day in WEEKDAYS}
    for ts in timestamps:
        if ts.weekday in day_map:
            day_map[ts.weekday].total_consumption += ts.consumption
            day_map[ts.weekday].total_cost += ts.consumption * ts.price
    # Lisää tulokset listaan oikeassa järjestyksessä
    for day in WEEKDAYS:
        analysis.append(day_map[day])

def displayResults(analysis: list[DAY_USAGE]) -> None:
    """Tulostaa analyysin tulokset"""
    print("Analysing timestamps.")
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for day in analysis:
        print(f" - {day.weekday} usage {day.total_consumption:.2f} kWh, cost {day.total_cost:.2f} €")
    print("### Electricity consumption summary ###")

def main() -> None:
    """Pääohjelma"""
    print("Program starting.")

    timestamps: list[TIMESTAMP] = []
    analysis: list[DAY_USAGE] = []

    filename = input("Insert filename: ")
    readTimestamps(filename, timestamps)
    analyseTimestamps(timestamps, analysis)
    displayResults(analysis)

    print("Program ending.")

if __name__ == "__main__":
    main()
