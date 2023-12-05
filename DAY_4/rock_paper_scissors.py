rock_paper_scissors = ['rock', 'paper', 'scissors']

player_input = int(input('Do you choose rock(0), paper(1), or scissors(2)?'))
player_choice = rock_paper_scissors[player_input]

import random


computer_random_input = random.randint(0,2)
computer_choice = rock_paper_scissors[computer_random_input]

if player_choice == 'rock':
    if computer_choice == 'paper':
        print(f"Computer chose paper.\nYou lose!")
    elif computer_choice == 'scissors':
        print(f"Computer chose scissors.\nYou won!")
    else:
        print("Computer chose scissors.\nIt's a draw")
elif player_choice == 'paper':
    if computer_choice == 'scissors':
        print(f"Computer chose scissors.\nYou lose!")
    elif computer_choice == 'rock':
        print(f"Computer chose rock.\nYou win!")
    else:
        print(f"Computer chose paper.\nIt's a draw!")
else:
    if computer_choice == 'rock':
        print(f"Computer chose rock.\nYou lose!")
    elif computer_choice == 'paper':
        print(f"Computer chose paper.\nYou win!")
    else: 
        print(f"Computer chose scissors.\nIt's a draw!")


