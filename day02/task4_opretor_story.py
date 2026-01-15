# Asking the user for two numbers
num1 = int(input("Hey! Enter your first number: "))
num2 = int(input("Great! Now enter your second number: "))
print("\n Let's do some math magic!")
# Arithmetic operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("\n Time to compare them!")
# Comparison
print("Are they equal?", num1 == num2)
print("Is the first number bigger?", num1 > num2)
print("Is the second number bigger?", num1 < num2)
print("\n Final Decision:")
# Logical decision using if-else
if num1 > num2:
    print("The first number is the boss ")
elif num1 < num2:
    print("The second number is the boss ")
else:
    print("Both numbers are twins ")
