"""
By:         Callum Clegg
Date:       14/01/2023

Desc:       Basic introduction to python for beginners. 
            Introducing to reading code, refactoring and documentation
"""

import random
from collections import defaultdict

game_stats: dict[str, int] = defaultdict(int,
    {
        "games_played": 1,
        "games_won":    0,
        "games_lost":   0
    }
)

def guessing_game() -> dict[str, int]:
    """ This function begins the guessing game. """
    number_of_attempts: int = 0

    while number_of_attempts < 3:
        target_number:      int = random.randint(1, 10)
        attempt:            int

        while True:
            user_input = input("Please guess a number between 1 and 10: ")
            if is_valid(user_input):
                attempt = int(user_input)
                break
            print("'{0}' is invalid.".format(user_input))

        if attempt == target_number:
            if check_continue_playing(input("Congradulations you have guessed the correct number! Play again? y/n: ")):
                game_stats["games_won"] += 1
                guessing_game()
            return dict(game_stats)
         
        print("{0} is {1} than target.".format(attempt, ("less", "greater")[attempt > target_number]))
        number_of_attempts += 1

    game_stats["games_lost"] += 1
    if check_continue_playing(input("You lost!, try again? y/n: ")):
        guessing_game()

    game_stats["games_played"] = game_stats["games_lost"] + game_stats["games_won"]

    return dict(game_stats)

def check_continue_playing(user_input: str) -> bool | str:
    """ Check if user wants to play again. """

    switcher: dict[str, bool] = {
        "yes": True,
        "y": True,
        "n": False,
        "no": False
    }

    return switcher.get(user_input.lower(), False)

def is_valid(user_answer: str) -> bool:
    """Check if the user input is infact allowed."""
    return user_answer.isdigit() and 1 <= int(user_answer) <= 10

if __name__ == "__main__":
    print("game_stats: {0}".format(guessing_game()))
    print("Program ended.")
