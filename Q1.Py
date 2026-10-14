username = input("Enter your username: ")

if len(username.strip()) < 5:
    print("Invalid username: Must contain at least 5 characters.")
elif username.strip().lower() == "admin":
    print("Invalid username: 'admin' is not allowed.")
else:
    print("Valid username.")
