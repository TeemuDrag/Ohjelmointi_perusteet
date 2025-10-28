import hashlib  # Tuodaan kirjasto salasanan tiivistämistä varten (hashaus)

# Vakioarvot
CREDENTIALS_FILE = "credentials.txt"  # Tiedosto, johon käyttäjätiedot tallennetaan
DELIMITER = ";"  # Erotinmerkki tiedoston riveillä

def hash_password(password: str) -> str:
    """
    Luo annetusta salasanasta MD5-tiivisteen (hashin).
    Tätä käytetään, jotta salasanoja ei tallenneta selväkielisenä.

    Esimerkki:
        >>> hash_password("salasana123")
        '4e7e6e92b9b1c8c899b9b2bb95b3f0b1'
    """
    return hashlib.md5(password.encode()).hexdigest()

def read_credentials() -> list[tuple[str, str, str]]:
    """
    Lukee käyttäjätiedot tiedostosta ja palauttaa listan käyttäjätiedoista.
    Jokainen käyttäjä esitetään tuplena (id, käyttäjänimi, salasana_hash).

    Esimerkki:
        credentials.txt sisältää:
        0;admin;58d613129c5e71de57ee3f44c5ce16bc

        >>> read_credentials()
        [('0', 'admin', '58d613129c5e71de57ee3f44c5ce16bc')]
    """
    users = []
    try:
        with open(CREDENTIALS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(DELIMITER)
                if len(parts) == 3:
                    users.append(tuple(parts))
    except FileNotFoundError:
        # Jos tiedostoa ei ole, palautetaan tyhjä lista
        pass
    return users

def write_credentials(users: list[tuple[str, str, str]]) -> None:
    """
    Tallentaa annetun käyttäjälistan tiedostoon.
    Jokainen käyttäjä kirjoitetaan muodossa: id;käyttäjänimi;hash

    Esimerkki:
        >>> write_credentials([("0", "admin", "abc123hash")])
        # credentials.txt sisältää nyt:
        0;admin;abc123hash
    """
    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as file:
        for user in users:
            file.write(DELIMITER.join(user) + "\n")

def register_user() -> None:
    """
    Luo uuden käyttäjän:
    - Kysyy käyttäjänimen ja salasanan
    - Luo käyttäjälle ID:n
    - Hashaa salasanan
    - Tallentaa uuden käyttäjän tiedostoon

    Esimerkki (käyttäjän syöte):
        Insert username: John
        Insert password: Secret123
        credentials.txt: 0;John;202cb962ac59075b964b07152d234b70
    """
    users = read_credentials()
    username = input("Insert username: ")
    password = input("Insert password: ")

    user_id = str(len(users))  # Käyttäjän ID määräytyy listan pituuden mukaan
    hashed = hash_password(password)

    users.append((user_id, username, hashed))
    write_credentials(users)
    print(f"User '{username}' registered successfully!\n")


# ---------------------------------------------
# FUNKTIO: login
# ---------------------------------------------
def login() -> tuple[str, str] | None:
    """
    Tarkistaa käyttäjän kirjautumistiedot:
    - Kysyy käyttäjänimen ja salasanan
    - Vertailee salasanaa tiedostossa olevaan tiivisteeseen

    Palauttaa (user_id, username), jos kirjautuminen onnistuu.
    Palauttaa None, jos epäonnistuu.

    Esimerkki:
        Insert username: John
        Insert password: Secret123
        Authentication successful!
    """
    users = read_credentials()
    username = input("Insert username: ")
    password = input("Insert password: ")
    hashed = hash_password(password)

    for user_id, name, stored_hash in users:
        if name == username:
            if stored_hash == hashed:
                print("Authentication successful!\n")
                return user_id, name
            else:
                print("Authentication failed!\n")
                return None
    print("Authentication failed!\n")
    return None
def user_menu(user_id: str, username: str) -> None:
        print("User menu:")
        print("1 - View profile")
        print("2 - Change password")
        print("0 - Logout")
        choice = input("Your choice: ")

        if choice == "1":
            print(f"Profile ID {user_id} - {username}\n")
        elif choice == "0":
            print("Logging out...\n")
        elif choice == "2":
            print("Change password not implemented.\n")
        else:
            print("Unknown option.\n")

def main() -> None:
    print("Program starting.")
    while True:  # 👈 silmukka alkaa tästä
        print("Options:")
        print("1 - Login")
        print("2 - Register")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            logged_user = login()
            if logged_user:
                user_menu(*logged_user)
        elif choice == "2":
            register_user()
        elif choice == "0":
            print("Exiting program.\n")
            break  # ✅ nyt toimii, koska ollaan silmukassa
        else:
            print("Unknown option.\n")

    print("Program ending.")  # tämä suoritetaan breakin jälkeen



# Käynnistää ohjelman vain, jos tiedosto suoritetaan suoraan
if __name__ == "__main__":
    main()
