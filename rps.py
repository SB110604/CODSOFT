import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    """Display the user's choice, the computer's choice, and the result."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    """Main function to play the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScores:\nYou: {user_score}\nComputer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nFinal Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing!")

# Start the game
play_game()
