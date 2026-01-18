def greet_user(name, role="student"):
    if role == "student":
        return f"Welcome student {name}"
    elif role == "admin":
        return f"Welcome admin {name}"

# Call the function once with only the name
print(greet_user("anamika"))

# Call the function with name and role
print(greet_user("utkarsh", role="admin"))