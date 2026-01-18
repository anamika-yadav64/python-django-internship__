def student_profile(name, **details):
    print(f"Student's Name: {name}")
    
    if details:
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No additional info")

# Example usage
student_profile("anamika", age=20, course="Computer Science", city="kotma")
student_profile("utkarsha")