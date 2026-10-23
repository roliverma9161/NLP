def run_quiz(questions):
    score = 0
    for q, a in questions.items():
        user_answer = input(f"{q}?: ").strip().lower()
        if user_answer == a.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {a}.\n")
    print(f"Quiz Over! Your score: {score}/{len(questions)}")

# flashcards = {"Capital of France": "Paris", "2 + 2": "4"}
# run_quiz(flashcards)