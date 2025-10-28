def askDimension(PPrompt: str) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed
print("Program starting.")

Width = askDimension("width")
Height = askDimension("height")
def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Area = PWidth * PHeight
   return Area

Area = calcRectangleArea(Width, Height)
print("")
print(f"Area is {Area}²")
print("Program ending")
