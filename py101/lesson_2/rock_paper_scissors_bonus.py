# Imports
import random
import math

# Helper functions
def prompt(message):
    print(f'==> {message}')

def compute_round_winner(user_choice, computer_choice):
    if ((user_choice == 's' and computer_choice == 'p') or      # scissors cuts paper
        (user_choice == 'p' and computer_choice == 'r') or      # paper covers rock
        (user_choice == 'r' and computer_choice == 'l') or      # rock crushes lizard
        (user_choice == 'l' and computer_choice == 'sp') or     # lizard poisons spock
        (user_choice == 'sp' and computer_choice == 'sc') or    # spock smashes scissors
        (user_choice == 'sc' and computer_choice == 'l') or     # scissors decapitates lizard
        (user_choice == 'l' and computer_choice == 'p') or      # lizard eats paper
        (user_choice == 'p' and computer_choice == 'sp') or     # paper disproves spock
        (user_choice == 'sp' and computer_choice == 'r') or     # spock vaporizes rock
        (user_choice == 'r' and computer_choice == 's')):       # rock crushes scissors
        round_winner = "You"
    elif user_choice == computer_choice:
        round_winner = "No one"
    else:
        round_winner = "The computer"

    return round_winner

def display_round_winner(round_winner):
    prompt(f"{round_winner} won the round!")
    
def update_scores(round_winner, user_score, computer_score):
    match round_winner:
        case "You":
            user_score += 1
        case "The computer":
            computer_score += 1

    return user_score, computer_score

def display_current_score(user_score, computer_score):
    prompt(f"Your score: {user_score} | Computer's score: {computer_score}")

def display_game_winner(best_of, score_cap, user_score, computer_score):
    if user_score == score_cap:
        prompt(f"You won the best of {best_of}!")
    elif computer_score == score_cap:
        prompt(f"The computer won the best of {best_of}!")


# One round of rock, paper, scissors
def rock_paper_scissors(user_score, computer_score):
    VALID_CHOICES = ['(r)ock', '(p)aper', '(sc)rissors', '(l)izard', '(sp)ock']
    VALID_ABBREVIATIONS = ['r', 'p', 'sc', 'l', 'sp']
    VALID_DICTIONARY = {'r': 'rock', 'p': 'paper', 'sc': 'scissors', 'l': 'lizard', 'sp': 'spock'}

    # Request user choice
    prompt(f"Your choice... {", ".join(VALID_CHOICES)}? ")
    user_choice = input()
    user_choice = user_choice[0].lower() if len(user_choice) == 1 else user_choice[:2].lower()

    # Validate user choice
    while user_choice not in VALID_ABBREVIATIONS:
        prompt(f"Please choose {", ".join(VALID_CHOICES)}.")
        user_choice = input().lower()

    # Request computer choice
    computer_choice = random.choice(VALID_ABBREVIATIONS)

    # Display player choices
    prompt(f"You chose {VALID_DICTIONARY[user_choice]} \
and the computer chose {VALID_DICTIONARY[computer_choice]}.")

    # Compute round winner
    round_winner = compute_round_winner(user_choice, computer_choice)

    # Display round winner
    display_round_winner(round_winner)

    # Update scores
    user_score, computer_score = update_scores(round_winner, user_score, computer_score)

    # Display current score
    display_current_score(user_score, computer_score)
    
    prompt("------------------------------------------------------------")
    return user_score, computer_score


# Play rock, paper, scissors, lizard, spock best of...
def play_best_of(best_of):
    score_cap = math.ceil(best_of / 2)
    
    user_score = 0
    computer_score = 0

    while (user_score < score_cap) and (computer_score < score_cap):
        user_score, computer_score = rock_paper_scissors(user_score, computer_score)

    display_game_winner(best_of, score_cap, user_score, computer_score)


# Initial play
play_best_of(5)
