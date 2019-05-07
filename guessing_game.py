"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game(highscore=999):
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    answer = random.randint(1, 10)
    tries = 0
    highscore = highscore

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
                        retry = input("Would you like to play again? [y]es/[n]o:  ")
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

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    print("------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("------------------------------------")
    print("                                    ")

    start_game()
