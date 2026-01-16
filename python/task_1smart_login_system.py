# Smart Login System

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "python123":
    print("Login Successful ")

elif username == "admin" and password != "python123":
    print("Wrong Password ")

else:
    print("User Not Found ")
