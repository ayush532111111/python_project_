import random
import time

def roll_dice():
    print("Rolling the dice...")
    time.sleep(1)  # Add a delay for effect
    return random.randint(1, 6)

def greet():
    print("Welcome to the Roll the Dice Game!")
    print("Let's see what you roll...")

def farewell():
    print("Thanks for playing Roll the Dice!")
    print("Hope you had fun!")

def main():
    greet()
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled: {result}")

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    farewell()

if __name__ == "__main__":
    main()
