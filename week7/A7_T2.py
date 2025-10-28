# Ohjelma: Pilkuilla erotettujen kokonaislukujen käsittelijä
# Tehtävä: Käyttäjä syöttää listan kokonaislukuja pilkuilla erotettuna.
# Ohjelma tarkistaa syötteen, ilmoittaa virheellisistä arvoista,
# laskee kelvollisten lukujen summan ja kertoo, onko summa parillinen vai pariton.

print("Program starting.")

# 1️⃣ Pyydetään käyttäjältä syöte – pilkuilla erotettu lista
user_input = input("Insert comma separated integers: ")

# 2️⃣ Pilkotaan syöte pilkun kohdalta osiin
# .split(",") tekee listan, jossa jokainen arvo on merkkijonona
items = user_input.split(",")

# 3️⃣ Luodaan tyhjä lista kelvollisille kokonaisluvuille
valid_numbers: list[int] = []

# 4️⃣ Käydään jokainen syötteen osa läpi ja tarkistetaan, onko se kokonaisluku
for item in items:
    # Poistetaan mahdolliset välilyönnit alusta ja lopusta
    value = item.strip()
    if value == "":
        continue  # ohitetaan tyhjät arvot, jos käyttäjä laittoi tuplapilkkuja
    try:
        # Muutetaan merkkijono kokonaisluvuksi
        number = int(value)
        valid_numbers.append(number)
    except ValueError:
        # Jos muunnos epäonnistuu, ilmoitetaan virheestä
        print(f"Error: '{value}' is not a valid integer and was skipped.")

# 5️⃣ Tarkistetaan, löytyikö yhtään kelvollista lukua
if len(valid_numbers) == 0:
    print("No valid integers to analyze.")
else:
    # 6️⃣ Lasketaan summa ja määrät
    total = sum(valid_numbers)
    count = len(valid_numbers)

    # 7️⃣ Tarkistetaan, onko summa parillinen vai pariton
    if total % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    # 8️⃣ Näytetään tulokset käyttäjälle
    print(f"There are {count} integers in the list.")
    print(f"Sum of the integers is {total} and it's {parity}")

# 9️⃣ Lopuksi ohjelma ilmoittaa päättymisestään
print("Program ending.")
