import string

LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(char: str, alphabet: str) -> str:
    """Siirtää yksittäistä merkkiä ROT13-säännön mukaisesti."""
    index = (alphabet.index(char) + 13) % 26
    return alphabet[index]


def rot13(text: str) -> str:
    """ROT13-salaus koko tekstille."""
    result = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            result += shiftCharacter(char, LOWER_ALPHABETS)
        elif char in UPPER_ALPHABETS:
            result += shiftCharacter(char, UPPER_ALPHABETS)
        else:
            result += char
    return result


def writeFile(filename: str, content: str) -> None:
    """Kirjoittaa koko sisällön tiedostoon yhdellä write()-kutsulla."""
    try:
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Error saving file: {e}")


def collect_texts() -> list[str]:
    """Kerää käyttäjältä rivejä, kunnes syötetään tyhjä rivi."""
    rows = []
    while True:
        line = input("Insert row (empty stops): ")
        if line == "":
            break
        rows.append(line)
    return rows


def main():
    print("Program starting.")
    print("\nCollecting plain text rows for ciphering.")

    plain_rows = collect_texts()
    ciphered_rows = [rot13(row) for row in plain_rows]
    ciphered_text = "\n".join(ciphered_rows) + "\n"

    print("\n#### Ciphered text ####")
    print(ciphered_text)
    print("#### Ciphered text ####\n")

    filename = input("Insert filename to save: ")
    writeFile(filename, ciphered_text)

    print("Ciphered text saved!")
    print("Program ending.")


if __name__ == "__main__":
    main()
