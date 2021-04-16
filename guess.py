#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sets up the game
"""
import logging
import random


class Guess:
    """
    The guess game class
    """

    guessed: bool = False

    def define_guess(self, guess_input: str) -> bool:
        """
        Define the guess
        :param guess_input s the number input
        :return: True if the guess is close to generated
        random number, false otherwise
        """
        number = random.randint(0, 350)
        guess = int(guess_input)

        if guess != number:
            print("You guessed wrong.")
            self.guessed = False
        else:
            print("You guessed correctly.")
            self.guessed = True
        return bool(self.guessed)

    def play_guess_game(self):
        """
        The play guess method
        :return:
        """
        guess = input("Enter a number between 0 and 350.")
        self.define_guess(guess)

        try_again = input("Do you want to try again? Answer with Yes or No.")

        if "Yes" in try_again:
            self.play_guess_game()
        else:
            print("Thanks for playing. Have a nice day! 😄")
