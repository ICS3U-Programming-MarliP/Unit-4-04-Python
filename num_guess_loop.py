#!usr/bin/env python3
# Created By: Marli Peters
# Date: Nov. 18, 2023
# This program sets a random correct answer between
# 1 and 10. If then asks the user to guess the number
# and repeats until they get it correct.
import random


def main():
    # set random number answer
    answer = random.randint(1, 9)

    while True:
        # get user guess
        guess_str = str(input("Guess random number between 1 and 9: "))
        print("")

        # catch invalid entries
        try:
            guess_int = int(guess_str)
        except Exception:
            print("Please enter a valid integer.")
            print("")
        else:
            # catch negative numbers
            if guess_int <= 0:
                print("Please enter a positive number.")
                print("")
            # catch numbers over 10
            elif guess_int > 9:
                print("Please only enter a number from 1 to 9.")
                print("")
            else:
                # check if guess is correct
                if guess_int == answer:
                    print("Your guess was correct!")
                    break
                else:
                    print("Your guess was incorrect! Please try again.")
                    print("")


if __name__ == "__main__":
    main()
