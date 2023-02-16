"""
By:         Callum Clegg
Date:       14/01/2023

Desc:       Basic introduction to python for beginners. 
            Introducing to reading code, refactoring and documentation
"""

import random

#      Consider doc comments, type safety and good variable names during this lab.

#   1. Try to create a basic guessing game algorithm that asks the user to guess any number between 1 and 10.
#      The user should get 3 chances to guess correctly, each time they guess incorrectly print if the number is 
#      greater or smaller than the target number. When all 3 lives are up end the game.

def guessing_game():
    pass


#   1a. ask the player if they would like to play again, this should return a bool value.
#       call this func inside guessing_game, if this func returns true then run game again, terminate otherwise.
def check_continue_playing(user_input):
    pass

#   1b. Check that the user input is infact correct (i.e., what happens if the user enters 'h' or '44'?), 
#       return a boolean to determine if the user input is infact valid for the game. 
#
#   1c. Use this func in guessing game and create a while loop condition to prevent the user progressing until a value is valid.
def is_valid() -> bool:
    pass

#   Bonus. store statistics of the game until terminatation (games played, lost and won).

if __name__ == "__main__":
    # Test Harness
    guessing_game()
