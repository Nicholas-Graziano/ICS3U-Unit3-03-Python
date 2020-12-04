#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if u got the right random number

import random

random_number = random.randint(1, 8)


def main():
    # this program checks if the random number is 5

    # input

    user_number = int(input("enter a number from 1, 8:"))

    # process
    if user_number == random_number:

        # output
        print("")
        print("You guessed correctly")
    else:
        print("you guessed incorrectly")


if __name__ == "__main__":
    main()
