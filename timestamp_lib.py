from datetime import datetime

# Vakioiden määrittely
MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list) -> None:
    """Lukee tiedoston rivit muodossa YYYY-MM-DDTHH:MM ja tallentaa datetime-olioina."""
    PTimestamps.clear()
    try:
        with open(PFilename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        dt = datetime.strptime(line, "%Y-%m-%dT%H:%M")  # Huomaa 'T'
                        PTimestamps.append(dt)
                    except ValueError:
                        print(f"Warning: '{line}' could not be parsed as datetime.")
    except FileNotFoundError:
        print(f'Error: File "{PFilename}" not found.')


def calculateYears(PYear: int, PTimestamps: list) -> int:
    return sum(1 for ts in PTimestamps if ts.year == PYear)

def calculateMonths(PMonth: str, PTimestamps: list) -> int:
    if PMonth not in MONTHS:
        return 0
    month_index = MONTHS.index(PMonth) + 1
    return sum(1 for ts in PTimestamps if ts.month == month_index)

def calculateWeekdays(PWeekday: str, PTimestamps: list) -> int:
    if PWeekday not in WEEKDAYS:
        return 0
    weekday_index = WEEKDAYS.index(PWeekday)
    return sum(1 for ts in PTimestamps if ts.weekday() == weekday_index)
