import MemoryGame
import GuessGame
import CurrencyRouletteGame
from Score import add_score

def welcome(name):
    return """Hello {0} and welcome to the World of Games (WoG).
Here you can find many cool games to play.""".format(name)


def load_game():
    flag = True
    while flag:
        game = input("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
Your choice: """)
        is_digit = game.isdigit()

        if is_digit:
            game = int(game)

            if 1 <= game <= 3:
                flag = False

    flag = True
    while flag:
        difficulty = input("Please choose game difficulty from 1 to 5: ")
        is_digit = difficulty.isdigit()

        if is_digit:
            difficulty = int(difficulty)

            if 1 <= difficulty <= 5:
                flag = False

    game_result = False

    if game == 1:
        game_result = MemoryGame.play(difficulty)
    elif game == 2:
        game_result = GuessGame.play(difficulty)
    else: 
        game_result = CurrencyRouletteGame.play(difficulty)

    if game_result:
        add_score(difficulty)
        print("You have won")
    else: 
        print("You have lost")
