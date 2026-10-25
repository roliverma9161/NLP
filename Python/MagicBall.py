import random
import time

def magic_8_ball():
    responses = [
        "It is certain.",
        "Without a doubt.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Don't count on it.",
        "Outlook not so good.",
        "Most likely.",
        "Signs point to yes."
    ]

    print("🔮 Welcome to the Python Oracle (Magic 8-Ball)")
    
    while True:
        question = input("\nAsk your yes/no question (or type 'quit'): ")
        if question.lower() == 'quit':
            print("Farewell, traveler.")
            break
        
        print("Consulting the spirits...")
        time.sleep(1) # Adds suspense
        print(f"Oracle says: {random.choice(responses)}")

# magic_8_ball()