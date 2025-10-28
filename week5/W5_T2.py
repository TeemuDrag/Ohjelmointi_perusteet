def frameWord(PWord):
    """Program starting."""
    frame_width = len(PWord) + 4  # 2 välilyöti + 2 sivu tähti
    print("*" * frame_width)
    print(f"* {PWord} *")
    print("*" * frame_width)
    return None


def main():
    """Main function to run the framed word program."""
    print("Program starting.")
    word = input("Insert a word: ")
    frameWord(word)
    print()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
