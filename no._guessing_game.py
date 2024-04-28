import random

def play_game():
    print("---------------------------------")
    print("WELCOME TO GUESS TWIST")
    print("---------------------------------")
    score = 0
    print("SCORE: 0")
    print()

    while True:
        guess = int(input("ENTER A NUMBER FROM 0-9: "))
        systm = random.randint(0, 9)
        print("PLAYER'S GUESS:", guess)
        print("SYSTEM'S GUESS:", systm)

        if guess != systm:
            score = score + abs(guess - systm)
            print("SCORE:", score)
        else:
            print()
            print("FINAL SCORE:", score)
            break

    print()
    print("GAME OVER!")

play_game()