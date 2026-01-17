password = "secret123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")
    attempts += 1
    
    if user_input == password:
        print("Access Granted")
        break
    elif attempts < max_attempts:
        print(f"Incorrect. {max_attempts - attempts} attempts remaining.")
    else:
        print("Account Locked")