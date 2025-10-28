import os
import codecs

#  Vakio
locations = ["home", "Galba's palace", "Otho's palace", "Vitellius' palace", "Vespasian's palace"]
progress_file = "player_progress.txt"

def rot13(text: str) -> str:
    """ROT13 cipher/decipher."""
    return codecs.encode(text, 'rot_13')

def initialize_progress():
    """Luo alkuperäisen player_progress.txt tiedoston jos sitä ei ole."""
    if not os.path.exists(progress_file):
        with open(progress_file, "w", encoding="utf-8") as f:
            f.write("current_location;next_location;passphrase\n")
            # Ensimmäinen lähtö: home -> Galba
            f.write(f"0;1;{rot13('discipline')}\n")  # qvfpvcyvar
        print("[Game] Progress initialized!")

def read_progress():
    #Lue viimeisin edistymisrivi tiedostosta.#
    if not os.path.exists(progress_file):
        initialize_progress()
    with open(progress_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if len(lines) < 2:
            return None  # Ei vielä dataa
        last_line = lines[-1].strip()
        current_id, next_id, passphrase_ciphered = last_line.split(";")
        return int(current_id), int(next_id), passphrase_ciphered

def save_progress(current, next_loc, passphrase):
    #Tallentaa edistymisen player_progress.txt tiedostoon.
    with open(progress_file, "a", encoding="utf-8") as f:
        f.write(f"{current};{next_loc};{passphrase}\n")
    print("[Game] Progress autosaved!")

def travel():
    print("Travel starting.")
    
    progress = read_progress()
    if not progress:
        print("No progress found. Initializing...")
        initialize_progress()
        progress = read_progress()
    
    current_id, next_id, passphrase_ciphered = progress
    current_loc = locations[current_id]
    next_loc = locations[next_id]
    passphrase_plain = rot13(passphrase_ciphered)
    
    print(f"Currently at {current_loc}.")
    print(f"Travelling to {next_loc}...")
    print(f"...Arriving to the {next_loc}.")
    print("Passing the guard at the entrance.")
    print(f'"{passphrase_plain.capitalize()}!"')
    
    # Viesti tiedosto oletetaan: "{NextLocationId}_{PassPhrase}.gkg"
    message_file = f"{next_id}_{passphrase_ciphered}.gkg"
    if os.path.exists(message_file):
        print("Looking for the message in the palace...")
        with open(message_file, "r", encoding="utf-8") as f:
            ciphered_message = f.readline().strip()
        print("Ah, there it is! Seems cryptic.")
        
        save_progress(current_id, next_id, passphrase_ciphered)
        
        print("Deciphering Emperor's message...")
        plain_message = rot13(ciphered_message)
        
        # Tallennetaan plain text
        plain_file = f"{next_id}-{passphrase_plain}.txt"
        with open(plain_file, "w", encoding="utf-8") as f:
            f.write(plain_message)
        
        print("Looks like I've got now the plain version copy of the Emperor's message.")
    else:
        print(f"No message file found: {message_file}")
    
    print("Time to leave...")
    print("Travel ending.")

#Pääohjelma
if __name__ == "__main__":
    travel()
