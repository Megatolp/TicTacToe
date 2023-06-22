from game import TicTacToe
from os import system
import os

__author__ = "pizzaburger"
__version__ = "0.0.0"
__license__ = "MIT"


def clear_screen():
 # Clear board
    if os.name == "nt":
        system("cls")
    else:
        system("clear")

if __name__ == "__main__":
    """ This is executed when run from the command line """

    # Init main game
    main_game = TicTacToe()


    while main_game.running:
        clear_screen()

        # Print board
        main_game.print_board()
        print(f"Player{ ' one' if main_game.playerone_turn else 'two' }, enter coordinate, indexed 0, comma separated as: 0,2")
        
        # str => int
        inp_x,inp_y = [int(x) for x in input().split(",")]
        main_game.play_turn(inp_x,inp_y)

        print("Win!!!!!!!!" if main_game.check_win() else "as" )
        pass


