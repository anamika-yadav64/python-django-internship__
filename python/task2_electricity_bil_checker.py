# Electricity Bill Checker

units = int(input("Enter the number of units consumed: "))

if units < 100:
    print("No Charge ")

elif units >= 100 and units <= 300:
    print("Normal Usage ")

else:
    print("High Usage – Save Energy! ")
