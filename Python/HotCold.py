import random

def hot_cold_game():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    prev_diff = None

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number:
            print(f"🎉 You got it! The number was {number}.")
            break

        diff = abs(number - guess)
        if prev_diff is None:
            print("🔥 Warm start!")
        elif diff < prev_diff:
            print("🔥 Getting HOTTER!")
        else:
            print("❄️ Getting COLDER!")
        
        prev_diff = diff

# hot_cold_game()