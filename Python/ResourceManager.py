def text_survival():
    food = 5
    wood = 5

    print("🌲 Welcome to Woods Survival! Survive for 5 days.")

    for day in range(1, 6):
        print(f"\n--- DAY {day} ---")
        print(f"Inventory -> Food: {food} | Wood: {wood}")
        
        if food <= 0 or wood <= 0:
            print("💀 You ran out of vital resources. Game Over!")
            return

        action = input("What will you do? [1] Hunt for Food [2] Gather Wood: ")
        
        if action == "1":
            food += 2
            wood -= 1
            print("You went hunting. Gained 2 food, but used 1 wood for warmth/fire.")
        elif action == "2":
            wood += 2
            food -= 1
            print("Você collected wood. Gained 2 wood, but used 1 food for energy.")
        else:
            print("Indecision cost you! You wasted time and lost 1 food and 1 wood.")
            food -= 1
            wood -= 1

    print("\n🏆 Congratulations! You survived the 5 days!")

# text_survival()