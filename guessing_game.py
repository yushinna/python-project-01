"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game(highscore=999):
    answer = random.randint(1, 10)
    tries = 0

    while True:
        try:
            guess = int(input("Pick a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                raise ValueError
        except ValueError:
            print("Oops! That was no valid number. Try again...")
        else:
            tries += 1
            if guess > answer:
                print("It is lower!")
                continue
            elif guess < answer:
                print("It is higher!")
                continue
            elif guess == answer:
                print("You got it! It took you {} tries.".format(tries))
                if highscore > tries:
                    highscore = tries
                while True:
                    try:
                        retry = input(
                            "Would you like to play again? [y]es/[n]o:  ")
                        if retry.lower() != "y" and retry.lower() != "yes" and retry.lower() != "n" and retry.lower() != "no":
                            raise ValueError
                    except ValueError:
                        print("Oops! That was no valid input. Try again...")
                    else:
                        if retry.lower() == "y" or retry.lower() == "yes":
                            print("                                    ")
                            print("The HIGHSCORE is {}.".format(highscore))
                            start_game(highscore)
                        elif retry.lower() == "n" or retry.lower() == "no":
                            print("                                    ")
                            print("The HIGHSCORE is {}.".format(highscore))
                            print("Closing game, see you next time!")
                        break
            break


def welcome():
    print("------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("------------------------------------")
    print("                                    ")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    welcome()
    start_game()
