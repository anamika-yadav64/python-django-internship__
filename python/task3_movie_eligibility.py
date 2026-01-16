# Entry Check System
age = int(input("Enter your age: "))
id_card = input("Do you have an ID card? (yes/no): ").lower()
if age >= 18 and id_card == "yes":
    print("Entry Allowed ")
else:
    print("Entry Denied ")