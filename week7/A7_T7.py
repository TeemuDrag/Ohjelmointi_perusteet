import string

ALPHABET = string.ascii_uppercase  # 'A'–'Z'

def load_config(filename):
    """Lataa roottorit ja heijastimen konfiguraatiotiedostosta"""
    rotors = []
    reflector = ""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("Rotor"):
                    rotors.append(line.split(":")[1])
                elif line.startswith("Reflector"):
                    reflector = line.split(":")[1]
        if len(rotors) != 3 or not reflector:
            raise ValueError("Configuration file must have 3 rotors and 1 reflector.")
        return rotors, reflector
    except FileNotFoundError:
        print(f'Error: Configuration file "{filename}" not found.')
        return None, None
    except Exception as e:
        print(f"Error reading config: {e}")
        return None, None


def rotate_rotors(positions):
    """Pyöritetään roottoreita enkoodausjärjestyksen mukaisesti"""
    positions[0] = (positions[0] + 1) % 26
    if positions[0] == 0:
        positions[1] = (positions[1] + 1) % 26
        if positions[1] == 0:
            positions[2] = (positions[2] + 1) % 26


def encode_char(c, rotors, reflector, positions):
    """Koodaa yhden kirjaimen (symmetrinen salaus/purku)"""
    if c not in ALPHABET:
        return c

    # 1️⃣ Eteenpäin roottorien läpi
    idx = ALPHABET.index(c)
    for rotor, pos in zip(rotors, positions):
        shifted = (idx + pos) % 26
        letter = rotor[shifted]
        idx = (ALPHABET.index(letter) - pos) % 26

    # 2️⃣ Heijastin
    letter = reflector[idx]
    idx = ALPHABET.index(letter)

    # 3️⃣ Takaisin roottorien läpi (käänteinen järjestys)
    for rotor, pos in zip(reversed(rotors), reversed(positions)):
        shifted = (idx + pos) % 26
        letter = ALPHABET[rotor.index(ALPHABET[shifted])]
        idx = (ALPHABET.index(letter) - pos) % 26

    return ALPHABET[idx]


def main():
    print("Program starting.")

    config_file = input("Insert config(filename): ")
    rotors, reflector = load_config(config_file)
    if not rotors or not reflector:
        return

    plugs = input("Insert plugs (y/n)?: ").strip().lower()
    if plugs != "y":
        print("No extra plugs inserted.")

    print("Enigma initialized.\n")

    while True:
        positions = [0, 0, 0]  # nollataan joka rivillä
        row = input("Insert row (empty stops): ").upper()
        if not row:
            break

        converted = ""
        for char in row:
            encoded = encode_char(char, rotors, reflector, positions)
            print(f'Character "{char}" illuminated as "{encoded}"')
            converted += encoded
            rotate_rotors(positions)

        print(f'Converted row - "{converted}".\n')

    print("Enigma closing.")


main()
