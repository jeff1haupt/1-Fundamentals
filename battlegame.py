# character selection
def choose_character():
    while True:
        # characters
        wizard = "Wizard"
        wizard_hp = 70
        wizard_damage = 150 

        human = "Human"
        human_hp = 150 
        human_damage = 20

        elf = "Elf"
        elf_hp = 100
        elf_damage = 100

        christian_bale = "Christian Bale"
        bale_hp = 100
        bale_damage = 150

        dragon_hp = 300
        dragon_damage = 50 

        # character menu 
        print("1)   Wizard")
        print("2)   Elf")
        print("3)   Human")
        print("4)   Christian Bale")
        print("5)   Exit")
        user_choice = input("Choose your character: ")

        if user_choice == '1' or user_choice.lower() == 'wizard':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        
        if user_choice == '2' or user_choice.lower() == 'elf':
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break

        if user_choice == '3' or user_choice.lower() == 'human':
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break

        if user_choice == '4' or user_choice.lower() == 'Christian Bale':
            character = christian_bale
            my_hp = bale_hp
            my_damage = bale_damage
            break

        if user_choice == '5' or user_choice.lower() == 'exit':
            quit()

        print("Unknown character")

    print(f"You have chosen the character: {character}")
    print(f"Health: {my_hp}")
    print(f"Damage: {my_damage}\n")
    play_game(character, my_hp, my_damage, dragon_hp, dragon_damage)
    

# game play loop
def play_game(character, my_hp, my_damage, dragon_hp, dragon_damage):
    while True:
        dragon_hp -= my_damage 
        print(f"The {character} damaged the Dragon!")
        print(f"The Dragon's hitpoints are now: {dragon_hp}\n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle.")
            play_again = input("Do you want to play again? (y/n)")
            if play_again == 'y':
                print("\n")
                choose_character()
            else:
                quit()
        my_hp -= dragon_damage
        print(f"The Dragon strikes back at {character}")
        print(f"The {character}'s hitpoints are now: {my_hp}\n")
        if my_hp <= 0:
            print(f"The {character} has lost the battle.")
            play_again = input("Do you want to play again? (y/n)")
            if play_again == 'y':
                print("\n")
                choose_character()
            else:
                quit()

choose_character()