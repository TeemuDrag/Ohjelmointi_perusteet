print("Program starting.")
print("Insert two integers.")
num1=int(input("Insert first integer: "))
num2=int(input("Insert second integer: "))
print("Comparing inserted integers.")
sum= num1+num2
if num1>num2:
    print("First integer is greater.")
else:
    print("Second integer is greater.")
print()

print("Adding integers together")
print(num1,"+",num2,"=",sum)
print()
print("Checking the parity of the sum...")
if sum % 2 == 1:
    print("Sum is odd.")
else:
    print("Sum is even.")

print("Program ending.")