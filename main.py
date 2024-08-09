import random

def rock_paper_scissors():
    choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}
    computer_choice = random.choice(list(choices.keys()))
    user_choice = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please choose 'r', 'p', or 's'.")
        return

    print(f"You chose {choices[user_choice]}")
    print(f"Computer chose {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "s" and computer_choice == "p"):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    rock_paper_scissors()




         
 




