"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""


import random
import time
def title():
    print("\nThis game is called guess the number.\n\nI will ask you to guess a number between 1 and 10 \nand you have to guess until you get the right number.\nIf you guess wrong, try again.")

def game():
    num = random.randint(1, 10)
    guess = None

    while guess != num:
        guess = input("guess a number between 1 and 10: ")
        guess = int(guess)

        if guess == num:
            print("congratulations! you won!")
            break
        else:
            print("nope, sorry. try again!")
title()
time.sleep(10)
game()
