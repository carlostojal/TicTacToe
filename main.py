
from helpers import Helpers
from random import randint

player_coordinates = {"x": 0, "y": 0}
bot_coordinates = {"x": 0, "y": 0}

board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]

won = False
first_play = True

game_mode = Helpers.main_menu()

if game_mode != 0:
    while won == False:

        # human plays
        while board[player_coordinates["x"]][player_coordinates["y"]] != 0 or first_play == True:
            raw_coordinates = input("Coordinates (x:y): ")
            player_coordinates["x"] = int(raw_coordinates.split(":")[0]) - 1
            player_coordinates["y"] = int(raw_coordinates.split(":")[1]) - 1
            first_play = False
        board[player_coordinates["x"]][player_coordinates["y"]] = "X"
        won = Helpers.check_win(board)["victory"]
        # bot plays
        if won == False:
            while board[bot_coordinates["x"]][bot_coordinates["y"]] != 0: # generate new coordinates if the space was already filled
                bot_coordinates["x"] = randint(0, 2)
                bot_coordinates["y"] = randint(0, 2)
            board[bot_coordinates["x"]][bot_coordinates["y"]] = "O"

        won = Helpers.check_win(board)["victory"]

        Helpers.show_board(board)

    print("WINNER: " + str(Helpers.check_win(board)["winner"]))

    Helpers.show_board(board)
