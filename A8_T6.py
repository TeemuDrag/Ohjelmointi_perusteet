import svgwrite

def drawSquare(PDwg: svgwrite.Drawing) -> None:
    """Ask user for square data and draw it on the drawing."""
    print("Insert square")
    x = float(input("- Left edge position: "))
    y = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    # Lisää suorakulmio piirrokseen
    PDwg.add(svgwrite.shapes.Rect(
        insert=(x, y),
        size=(side, side),
        fill=fill,
        stroke=stroke
    ))
    print("Square added.\n")


def drawCircle(PDwg: svgwrite.Drawing) -> None:
    """Ask user for circle data and draw it on the drawing."""
    print("Insert circle")
    cx = float(input("- Center X: "))
    cy = float(input("- Center Y: "))
    radius = float(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    PDwg.add(svgwrite.shapes.Circle(
        center=(cx, cy),
        r=radius,
        fill=fill,
        stroke=stroke
    ))
    print("Circle added.\n")


def saveSvg(PDwg: svgwrite.Drawing) -> None:
    """Ask for filename and save the SVG drawing in pretty format."""
    filename = input("Insert filename: ").strip()

    print(f"Saving file to \"{filename}\"")
    confirm = input("Proceed (y/n)?: ").lower()

    if confirm == "y":
        # Tallenna tiedosto kauniissa muodossa, sisennys 2
        PDwg.pretty = True
        PDwg.saveas(filename)
        print("Vector saved successfully!\n")
    else:
        print("Save cancelled.\n")


def showOptions() -> None:
    """Display main menu options."""
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")


def main() -> None:
    """Main program logic."""
    print("Program starting.")

    # 1. Luodaan piirrosolio (Drawing)
    Dwg = svgwrite.Drawing()

    while True:
        showOptions()
        choice = input("Your choice: ").strip()

        if choice == "1":
            drawSquare(Dwg)
        elif choice == "2":
            drawCircle(Dwg)
        elif choice == "3":
            saveSvg(Dwg)
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:
            print("Unknown option.\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
