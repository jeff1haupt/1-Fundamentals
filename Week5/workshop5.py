import random



def main():
    user_control()

def guess_random_number(tries, start, stop): # task 1
    random_number = random.randint(start, stop)
    previous_guesses = [] # bonus task 3
    while True and tries != 0: # Bonus Task 1
        print(f'Number of tries remaining: {tries}')
        guess = int(input(f'Guess a number between {start} and {stop}: '))
        if start <= guess <= stop and guess not in previous_guesses:
            if guess == random_number:
                print('You guessed the correct number!')
                return 0
            elif guess < random_number: 
                tries -= 1
                if tries == 0:
                    print("You've run out of tries...")
                    return 0
                else:
                    print('Guess higher!')
                    previous_guesses.append(guess)
            else:
                tries -= 1
                if tries == 0:
                    print("You've run out of tries...")
                    return 0
                else:
                    print('Guess lower!')
                    previous_guesses.append(guess)
        else:
            if guess in previous_guesses:
                print("You've already picked that number...")
            else:
                print('The guess is outside the range of numbers, try again')

def guess_random_num_linear(tries, start, stop): # task 2
    random_number = random.randint(start, stop)
    print(f'The number for the program to guess is: {random_number}')
    print(f'Number of tries remaining: {tries}')
    for i in range(start, stop):
        print(f'The program is guessing... {i}')
        if i == random_number:
            print('The program has guessed the correct number!')
            return True
        else:
            tries -= 1
            if tries == 0:
                print('The program has failed to guess the correct number.')
                return False
        
def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop)
    print(f'Random number to find: {random_number}')
    initial_tries = tries
    left, right = start, stop
    while left <= right:
        if tries != 0:
            middle = (left + right) // 2

            if middle == random_number:
                print(f'Found it! {middle}')
                return 0
            
            if middle < random_number:
                print(f"Guessing higher than {middle}")
                left = middle + 1
                tries -= 1
            elif middle > random_number:
                print(f"Guessing lower than {middle}")
                right = middle - 1 
                tries -=1
        else:
            print(f'The program failed to find the number {random_number} in {initial_tries} tries.')
            return 0

def user_control(): # bonus task 2
    choice = input("Make your selection: \n1) You guess against a random number\n2) You play a gambling game to see if the computer can reach the correct number\n3) The computer guesses using binary search\n")
    if choice == '1':
        tries = int(input("Enter the number of tries you want to have: "))
        start = int(input("Enter the starting number of the number range: "))
        stop = int(input("Enter the ending number of the range: "))
        guess_random_number(tries, start, stop)
        return 0
    elif choice == '2':
        gamble()
        return 0
    else:
        tries = int(input("Enter the number of tries you want to have: "))
        start = int(input("Enter the starting number of the number range: "))
        stop = int(input("Enter the ending number of the range: "))
        guess_random_num_binary(tries, start, stop)
        return 0

def gamble():
    bank_roll = 10
    while True:
        if 0 < bank_roll < 51:
            player_bet = int(input("Place your bet ($1 to $10): "))
            if 1 <= player_bet <= 10 and player_bet <= bank_roll:
                if guess_random_num_linear(5, 1, 10):
                    bank_roll += player_bet
                    print(f'Your current bank roll: {bank_roll}')
                else:
                    bank_roll -= player_bet
                    print(f'Your current bank roll: {bank_roll}')
        else:
            if bank_roll <= 0:
                print('You lost all your money')
                break
            else:
                print('You won!')
                break
    return 0                

if __name__ == "__main__":
    main()