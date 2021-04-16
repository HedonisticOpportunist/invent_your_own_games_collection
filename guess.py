#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sets up the game
"""

import random


class Guess:
    """
    The guess game class
    """

    guessed: bool = False

    def define_guess(self, guess: int) -> bool:
        """
        Define the guess
        :param guess the number input
        :return: True if the guess is close to generated
        random number, false otherwise
        """
        number = random.randint(0, 350)
        guess_counter = 0

        while guess_counter < 6:
            guess_counter = guess_counter + 1
            if guess < number or guess > number:
                self.guessed = False
            else:
                self.guessed = True
                break
        return bool(self.guessed)

    def display_message(self, guess: int) -> str:
        """
        Displays a message regarding the game
        output
        :param guess
        :return: logging message
        """
        result = self.define_guess(guess)
        if result:
            return "You guessed right."
        else:
            return "You guessed wrong."

    def play_guess_game(self, guess: int):
        """
        The play guess method
        param: guess
        :return:
        """
        print(self.display_message(guess))
