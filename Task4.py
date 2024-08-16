''' TASK 4
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for
the computer.
Game Logic: Determine the winner based on the user's choice and the
omputer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock. Display Result: Show the user's choice and
the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and com '''

import random

# Initialize scores
user_score = 0
computer_score = 0

while True:
    # User Input: Prompt the user to choose rock, paper, or scissors
    user_choice = input("Enter your choice (rock, paper, or scissors): ")

    # Validate user input
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid input. Enter your choice (rock, paper, or scissors): ")

    # Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Display user's choice and computer's choice
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    # Game Logic: Determine the winner based on the user's choice and the computer's choice
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # Display scores
    print(f"Score - You: {user_score}, Computer: {computer_score}\n")

    # Play Again: Ask the user if they want to play another round
    play_again = input("Do you want to play again? (yes/no): ")
    while play_again not in ["yes", "no"]:
        play_again = input("Invalid input. Do you want to play again? (yes/no): ")

    if play_again == "no":
        break

print("Thanks for playing!")
