import random

def banner():
    f"""
  ____                           _       
 | __ )    __ _    __ _    ___  | |  ___ 
 |  _ \   / _` |  / _` |  / _ \ | | / __|
 | |_) | | (_| | | (_| | |  __/ | | \__ \
 |____/   \__,_|  \__, |  \___| |_| |___/
                  |___/                  
                  
Bagels, a deductive logic game.
I am thinking of a {NUM_DIGITS} digit number. Try to guess what it is.
Here are some clues:
When I say:
Pico    - One digit is correct but in the wrong position.
Fermi   - One digit is correct and in the right position.
Bagels  - No digit is correct.
I have thought up a number.
You have 10 guesses to get it.        

                [ v.1.0 ]
        [ Developer : Blesslin Jerish R ]
"""

