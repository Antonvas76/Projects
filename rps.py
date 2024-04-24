import math
import random

CHOICES = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}

def get_computer_choice():
    global CHOICES
    choices_arr = list(CHOICES.keys())
    return random.choice(choices_arr)

def get_user_choice():
    return input("\nPick one of the following: 'r' for rock, 'p' for paper, 's' for scissors\n").lower()

def determine_winner(user_choice, computer_choice):
    global CHOICES

    if user_choice == computer_choice:
        print(f'you and the computer have both chosen {CHOICES[user_choice]}. It\'s a tie.')
        return None
    elif (user_choice == 'r' and computer_choice == 's') or \
       (user_choice == 's' and computer_choice == 'p') or \
       (user_choice == 'p' and computer_choice == 'r'):
        print(f'The computer has chosen {CHOICES[computer_choice]}')
        print("YOU WIN!")
        return True
    else:
        print(f'The computer has chosen {CHOICES[computer_choice]}')
        print("YOU LOSE!")
        return False


def play():

    play_again = True
    while play_again:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        determine_winner(user_choice, computer_choice)
        is_play_again = input('To play again, say \'yes\'. \n')
        play_again = is_play_again.lower() in ['yes', 'y']

play()