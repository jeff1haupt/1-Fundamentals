from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {
    "admin": "password123"
}
donations = []
authorized_user = ""

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)

    choice = input("Choose an option: ")
    if choice == "1":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    elif choice == "2":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username, password)
        # password argument is part of bonus task
        if authorized_user != "":
            database[authorized_user] = password
    elif choice == "3":
        if authorized_user == "":
            print("\nYou are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
    elif choice == "4":
        show_donations(donations)
    elif choice == "5":
        print("\nLeaving DonateMe...")
        break
