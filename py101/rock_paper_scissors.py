# Imports
import random

# Helper functions
def prompt(message):
    print(f'==> {message}')

# The game of rock, paper, scissors
def rock_paper_scissors():
    VALID_CHOICES = ['rock', 'paper', 'scissors']
    
    prompt(f"Your choice... {", ".join(VALID_CHOICES)}? ")
    
    user_choice = input().lower()

    while user_choice not in VALID_CHOICES:
        prompt(f"Please choose {", ".join(VALID_CHOICES)}.")
        user_choice = input().lower()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {user_choice} and the computer chose {computer_choice}.")

    if ((user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')):
        prompt("You win!")
    elif user_choice == computer_choice:
        prompt("It's a tie!")
    else:
        prompt("The computer wins!")

    print("------------------------------------------------")

# The continuous option to play again
def play_rock_paper_scissors():
    while True:
        rock_paper_scissors()

        prompt("Play again? (yes/no)")
        play_again = input()

        if play_again[0].lower() == 'n':
            prompt("Thanks for playing!")
            break

# Initial play
play_rock_paper_scissors()
