#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main
"""
from guess import Guess

guess = Guess()
number = input("Enter a number between 0 and 350.")
guess.play_guess_game(int(number))



