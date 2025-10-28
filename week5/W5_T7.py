# Määritellään sanan erotinmerkki (pilkku)
DELIMITER = ','

def collectWords():
    """Kysyy käyttäjältä sanoja ja palauttaa ne yhtenä merkkijonona, jossa sanat erotetaan pilkulla."""
    ws = []  # Tyhjä lista, johon sanat kerätään

    # Kysytään sanoja niin kauan, kunnes käyttäjä painaa vain Enter
    while True:
        w = input("Insert word(empty stops): ").strip()  # Poistetaan mahdolliset ylimääräiset välilyönnit
        if w == "":  # Jos käyttäjä ei kirjoita mitään, lopetetaan kysely
            break
        ws.append(w)  # Lisätään sana listaan

    # Yhdistetään kaikki sanat yhdeksi merkkijonoksi, erotettuna DELIMITER-merkillä (pilkulla)
    return DELIMITER.join(ws)


def analyseWords(ws_str):
    """Ottaa vastaan pilkulla erotetut sanat ja laskee niiden määrän, merkkimäärän ja keskipituuden."""
    
    # Jos käyttäjä ei syöttänyt mitään sanoja
    if not ws_str:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return

    # Pilkotaan merkkijono takaisin listaksi pilkun kohdalta
    ws = ws_str.split(DELIMITER)

    # Lasketaan sanojen määrä
    sanat = len(ws)

    # Lasketaan kaikkien kirjainten määrä
    kirjaimet = sum(len(s) for s in ws)

    # Lasketaan sanojen keskimääräinen pituus
    avg = kirjaimet / sanat 

    # Tulostetaan tulokset
    print(f"- {sanat} Words")
    print(f"- {kirjaimet} Characters")
    print("- {:.2f} Average word length".format(avg))


def main():
    """Ohjelman pääfunktio  hoitaa päälogiikan."""
    print("Program starting.")
    collected = collectWords()     # Kutsutaan sanankeruufunktiota
    analyseWords(collected)        # Analysoidaan kerätyt sanat
    print("Program ending.")


# Käynnistetään ohjelma vain, jos tiedosto suoritetaan suoraan (ei tuoda toisesta tiedostosta)
if __name__ == "__main__":
    main()
