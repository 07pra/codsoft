import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("Rock-Paper-Scissors Game")
        print("------------------------")
        print("Choose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter your choice (1/2/3/4): ")

        if user_choice == '4':
            print("Thanks for playing!")
            break

        if user_choice not in ['1', '2', '3']:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
            continue

        user_choice = "rock" if user_choice == '1' else "paper" if user_choice == '2' else "scissors"
        computer_choice = random.choice(["rock", "paper", "scissors"])

        result = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(f"Result: {result}\n")

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
        print("------------------------")

if __name__ == "__main__":
    main()
