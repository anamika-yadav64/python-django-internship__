# Number Analyzer

for num in range(1, 21):  
    if num == 13:
        continue   # Skip number 13
    if num % 2 == 0:
        print(num, "- Even")
    else:
        print(num, "- Odd")