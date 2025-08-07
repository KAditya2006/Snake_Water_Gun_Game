# snake_water_gun_game_project.
import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif (comp == 's' and you == 'w') or (comp == 'w' and you == 'g') or (comp == 'g' and you == 's'):
        return False
    else:
        return True

print("Welcome to Snake, Water, Gun Game!")
print("Enter 's' for Snake, 'w' for Water, 'g' for Gun")
print("To exit the game at any time, type 'exit'\n")

while True:
    you = input("Your Turn: Snake(s), Water(w), or Gun(g)? ").lower()

    if you == 'exit':
        continue_choice = input("Are you sure you want to exit? (yes/no): ").lower()
        if continue_choice == 'yes':
            print("\nYou lose because you left the game.")
            print("Exiting the game...")
            print("Thanks for playing! Goodbye!")
        else:
            print("\nContinuing the game...\n")
            continue    
        break
    
    

    if you not in ['s', 'w', 'g']:
        print("❌ Invalid input! Please enter 's', 'w', or 'g'.\n")
        continue

    comp = random.choice(['s', 'w', 'g'])
    result = gameWin(comp, you)

    print(f"\nComputer chose: {comp}")
    print(f"You chose: {you}")

    if result is None:
        print("🤝 It's a tie!")
    elif result:
        print("🎉 You Win!")
    else:
        print("💥 You Lose!")
    print()  # spacing between rounds
