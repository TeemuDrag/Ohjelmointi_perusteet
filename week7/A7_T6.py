import random
random.seed(1234)  # Satunnaisuuden toistettavuus

# ASCII-kuvat
ROCK_ART = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER_ART = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS_ART = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Mapataan valinnat nimiin ja ASCII-kuviin
CHOICES = {
    1: ("rock", ROCK_ART),
    2: ("paper", PAPER_ART),
    3: ("scissors", SCISSORS_ART)
}

# Seurataan tuloksia
results = {
    "player": {"wins":0, "losses":0, "draws":0},
    "bot": {"wins":0, "losses":0, "draws":0}
}

# Pääohjelma
def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    bot_name = "RPS-3PO"
    print(f"Your opponent is {bot_name}.")
    print("Game starts...\n")

    while True:
        # Valikko
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        try:
            player_choice = int(input("Your choice: "))
        except ValueError:
            print("Invalid input, please enter a number 0-3.")
            continue

        if player_choice == 0:
            break
        if player_choice not in CHOICES:
            print("Invalid choice, select 1, 2 or 3.")
            continue

        # Botin valinta
        bot_choice = random.randint(1,3)

        # Tulostetaan valinnat
        print("\nRock! Paper! Scissors! Shoot!\n")
        print("#"*25)
        print(f"{player_name} chose {CHOICES[player_choice][0]}.\n")
        print(CHOICES[player_choice][1])
        print("#"*25)
        print(f"{bot_name} chose {CHOICES[bot_choice][0]}.\n")
        print(CHOICES[bot_choice][1])
        print("#"*25)

        # Selvitetään kierroksen tulos
        player_val = CHOICES[player_choice][0]
        bot_val = CHOICES[bot_choice][0]

        if player_val == bot_val:
            print(f"Draw! Both players chose {player_val}.")
            results["player"]["draws"] += 1
            results["bot"]["draws"] += 1
        elif (player_val == "rock" and bot_val == "scissors") or \
             (player_val == "paper" and bot_val == "rock") or \
             (player_val == "scissors" and bot_val == "paper"):
            print(f"{player_name} {player_val} beats {bot_name} {bot_val}.")
            results["player"]["wins"] += 1
            results["bot"]["losses"] += 1
        else:
            print(f"{bot_name} {bot_val} beats {player_name} {player_val}.")
            results["bot"]["wins"] += 1
            results["player"]["losses"] += 1
        print()  # Tyhjä rivi seuraavaa kierrosta varten

    # Lopputulokset
    print("\nResults:")
    print(f"{player_name} - wins ({results['player']['wins']}), losses ({results['player']['losses']}), draws ({results['player']['draws']})")
    print(f"{bot_name} - wins ({results['bot']['wins']}), losses ({results['bot']['losses']}), draws ({results['bot']['draws']})")
    print("\nProgram ending.")

# Käynnistetään peli
main()
