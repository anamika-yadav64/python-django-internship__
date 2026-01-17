# Let's explain how Python works using print statements!

print("=" * 60)
print("WHAT IS A PYTHON INTERPRETER?")
print("=" * 60)

print("\nImagine you're at a restaurant and you speak English,")
print("but the chef only understands French.")
print("You need a translator to convert your order into French.")
print("\nA Python interpreter is like that translator!")
print("It takes the Python code YOU write (English-like)")
print("and converts it into instructions the computer understands (machine language).")
print("\nThe interpreter reads your code line by line")
print("and tells the computer exactly what to do.")

print("\n" + "=" * 60)
print("HOW PYTHON CODE GETS EXECUTED STEP BY STEP")
print("=" * 60)

print("\nStep 1: You write Python code in a file")
print("  → Example: print('Hello World')")

print("\nStep 2: You run the file (python filename.py)")
print("  → The interpreter wakes up and starts reading")

print("\nStep 3: The interpreter reads your code line by line")
print("  → It doesn't read the whole file at once!")
print("  → It's like reading a book one sentence at a time")

print("\nStep 4: For each line, the interpreter checks:")
print("  → Is this valid Python syntax?")
print("  → Do the variables exist?")
print("  → What operation should I perform?")

print("\nStep 5: The interpreter converts Python into low-level commands")
print("  → These are instructions the CPU understands")

print("\nStep 6: The computer executes those commands")
print("  → Memory gets allocated, calculations happen, data is printed, etc.")

print("\nStep 7: Move to the next line and repeat!")

print("\n" + "=" * 60)
print("SIMPLE EXAMPLE:")
print("=" * 60)
print("\nWhen you write:")
print("  x = 5")
print("  print(x * 2)")
print("\nThe interpreter does this:")
print("  Line 1 → Create a variable 'x' and store the number 5 in memory")
print("  Line 2 → Take the value of x (5), multiply it by 2 (=10), print it")
print("  Line 3 → No more code? Done! Program finished.")