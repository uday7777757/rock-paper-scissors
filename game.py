import random

choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

print("Welcome to Rock-Paper-Scissors!")

while True:
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    if player_choice == "quit":
        print("Thanks for playing!")
        break
    if player_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    print(get_winner(player_choice, computer_choice))