import random

def play_rpsls():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    rules = {
        "scissors": ["paper", "lizard"],
        "paper": ["rock", "spock"],
        "rock": ["lizard", "scissors"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

    print("Choose: rock, paper, scissors, lizard, or spock (or 'quit')")

    while True:
        user = input("\nYour choice: ").lower()
        if user == "quit":
            break
        if user not in choices:
            print("Invalid choice, try again.")
            continue

        comp = random.choice(choices)
        print(f"Computer chose: {comp}")

        if user == comp:
            print("🤝 It's a tie!")
        elif comp in rules[user]:
            print("✨ You win!")
        else:
            print("💻 Computer wins!")

# play_rpsls()