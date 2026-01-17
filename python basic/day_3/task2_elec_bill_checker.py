# Electricity Bill Checker

units = int(input("Enter units consumed: "))

if units < 100:
    print("No Charge")
elif units <= 300:
    print("Normal Usage")
else:
    print("High Usage – Save Energy!")