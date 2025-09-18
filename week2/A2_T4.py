print("""Program starting." 
"Estimate how many minutes you spent on programming...""")
print()
t1=float(input("A1_T1: "))
t2=float(input("A1_T2: "))
t3=float(input("A1_T3: "))
t4=float(input("A1_T4: "))
t5=float(input("A1_T5: "))
t6=float(input("A1_T6: "))
t7=float(input("A1_T7: "))
t = [t1, t2, t3, t4, t5, t6, t7]
total = sum(t)
keski = sum(t) / len(t)
pyoristetty = round(keski)
print()
print("In total you spent",total,"minutes on programming.")
print(f"Average per task was {keski:.2f} min and same rounded to the nearest integer {int(pyoristetty)} \n min.")
print()
print("Program ending.")


