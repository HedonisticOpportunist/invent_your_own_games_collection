#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sets up the joke game
"""


class Jokes:
    """
    Sets up the jokes class
    """
    jokes = [
        "What do you get when you cross a snowman with a vampire?",
        "Frostbite!",
        "What do dentists call an astronaut's cavity?",
        "A black hole!",
        "Knock, knock!",
        "Who's there?",
        "Interrupting cow.",
        "Interrupting cow w-MOO!"
    ]

    def display_jokes(self):
        """
        Displays jokes
        :return:
        """
        print("**** Let the jokes begin ****")
        input()
        for joke in self.jokes:
            input()
            print(joke)
            print("********")
        input()
        print("***Hope you had a good laugh!***")

