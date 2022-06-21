import random

def banner():
        print(f"""
  ____                           _       
 | __ )    __ _    __ _    ___  | |  ___ 
 |  _ \   / _` |  / _` |  / _ \ | | / __|
 | |_) | | (_| | | (_| | |  __/ | | \__ \\
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
You have {MAX_GUESSES} guesses to get it.

                [ v.1.0 ]
        [ Developer : Blesslin Jerish R ]
""")


NUM_DIGITS = 2 # No of Digits to guess
MAX_GUESSES = 10 # Total number of guesses

def game():
        while True: # Main loop the game
                secretNum = getSecretNum()
                numGuesses = 1
                while numGuesses <= MAX_GUESSES:
                        guess = ''
                        # Keep looping untill they enter a valid guess:
                        while len(guess) != NUM_DIGITS or not guess.isdecimal():
                                print(f"Guess #{numGuesses}")
                                guess = input('> ')
                        clues = getClues(guess, secretNum)
                        print(clues)
                        numGuesses += 1

                        if guess == secretNum:
                                break # correct
                        if numGuesses > MAX_GUESSES:
                                print('You ran out of guesses')
                                print(f'The answer was {secretNum}')
                # Ask Player if they want to play again
                print("Do you want to play again ? [yes or no]")
                if not input('> ').lower().startswith('y'):
                        break
        print('Thanks for playing')

def getSecretNum():
        """Returns a string made up of NUM_DIGITS unique random digits"""
        numbers = list('0123456789')
        random.shuffle(numbers)

        # Get the first NUM_DIGITS digits in the list for the secret number
        secretNum = ''
        for i in range(NUM_DIGITS):
                secretNum += str(numbers[i])
        return secretNum

def getClues(guess, secretNum):
        """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
        if guess == secretNum:
                return 'You got it! Winner'
        clues = []
        for i in range(len(guess)):
                if guess[i] == secretNum[i]:
                        # A correct digit is in the correct place.
                        clues.append('Fermi')
                elif guess[i] in secretNum:
                        # A correct digit is in the incorrect place.
                        clues.append('Pico')
                if len(clues) == 0:
                        return 'Bagels' # There are no correct digits at all.
                else:
                        # Sort the clues into alphabetical order so their original order
                        # doesn't give information away.
                        clues.sort()
                        # Make a single string from the list of string clues.
                        return ' '.join(clues)

def main():
    banner()
    game()

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
        main()