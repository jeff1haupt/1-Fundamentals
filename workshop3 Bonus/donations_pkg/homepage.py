def show_homepage():
    print("\n       === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.   Login       | 2.   Register        |")
    print("------------------------------------------")
    print("| 3.   Donate      | 4.   Show Donations  |")
    print("------------------------------------------")
    print("|              5.   Exit                  |")
    print("------------------------------------------")


def donate(username):
    donation_amt = float(input("\nEnter amount to donate: "))
    donation = username + " donated $" + str(donation_amt)
    print("Thank you for your donation!")
    return donation


def show_donations(donations):
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        total = 0                           # bonus
        for donation in donations:
            print(donation)
            idx = donation.find('$') + 1    # bonus
            total += float(donation[idx:])  # bonus
        print("Total = $" + str(total))     # bonus
