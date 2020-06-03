
from helpers import Helpers
from random import randint

player_coordinates = {"x": 0, "y": 0}
player1_coordinates = {"x": 0, "y": 0}

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

        # human (this) plays
        while board[player_coordinates["x"]][player_coordinates["y"]] != 0 or first_play == True:
            raw_coordinates = input("Coordinates (x:y): ")
            player_coordinates["x"] = int(raw_coordinates.split(":")[0]) - 1
            player_coordinates["y"] = int(raw_coordinates.split(":")[1]) - 1
            first_play = False
        board[player_coordinates["x"]][player_coordinates["y"]] = "X"
        won = Helpers.check_win(board)["victory"]
        # bot / other player plays
        if won == False:
            if game_mode == 1:
                while board[player1_coordinates["x"]][player1_coordinates["y"]] != 0: # generate new coordinates if the space was already filled
                    player1_coordinates["x"] = randint(0, 2)
                    player1_coordinates["y"] = randint(0, 2)
            board[player1_coordinates["x"]][player1_coordinates["y"]] = "O"

        won = Helpers.check_win(board)["victory"]

        Helpers.show_board(board)

    print("WINNER: " + str(Helpers.check_win(board)["winner"]))

    Helpers.show_board(board)
