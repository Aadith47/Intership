var1=float(input("Enter the temprature "))
choice=(input("Convert into Celcius:C Fahrenheit:F  "))
if choice == "C":
    print((var1 - 32) * 5/9)
elif choice == "F":
    print((var1 * 9/5) + 32)
else:
    print("Invalid Choice")