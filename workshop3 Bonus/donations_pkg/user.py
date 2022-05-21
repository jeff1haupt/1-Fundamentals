def login(database, username, password):
    if username.lower() in database:            # .lower() is for bonus task
        if password == database[username]:
            print("\nWelcome back", username + "!")
            return username
        print("\nIncorrect password for", username + ".")
        return ""

    print("\nUser not found. Please register.")
    return ""


def register(database, username, password):
    if username.lower() in database:            # .lower() is for bonus task
        print("\nUsername already registered.")
        return ""
    if len(username) > 10:
        print("Username must be less than 10 characters")
        return ""
    if len(password) <= 5:
        print("Password must be more than 5 characters")
        return ""

    print("\nUsername " + username, "registered!")
    return username.lower()                     # .lower() is for bonus task
