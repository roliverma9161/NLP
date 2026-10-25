import random

def password_hacker():
    words = ["CODE", "BYTE", "DATA", "NODE", "JAVA", "CHIP", "DISK"]
    secret = random.choice(words)
    attempts = 4

    print("--- SECURE TERMINAL ACCESS ---")
    print("Guess the 4-letter password. You have 4 attempts.")

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}/{attempts}: ").upper()
        
        if len(guess) != 4:
            print("Password must be exactly 4 letters!")
            continue

        if guess == secret:
            print("🔓 ACCESS GRANTED! You successfully hacked the system.")
            return

        # Give feedback
        exact_matches = sum(1 for a, b in zip(guess, secret) if a == b)
        partial_matches = sum(min(guess.count(c), secret.count(c)) for c in set(guess)) - exact_matches

        print(f"Feedback -> Correct Position: {exact_matches} | Wrong Position: {partial_matches}")

    print(f"🔒 ACCESS DENIED! The correct password was {secret}.")

# password_hacker()