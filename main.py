
from helpers import Helpers
from random import randint
import socket

player_coordinates = {"x": 0, "y": 0}
player1_coordinates = {"x": 0, "y": 0}

board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]

PORT = 2911

won = False
first_play = True

game_mode = Helpers.main_menu()
online_mode = 0
s = "this_will_be_the_socket"
username = "player"
opponent_name = "player1"

if game_mode != 0:
    if game_mode == 2: # online menu
        online_mode = Helpers.online_menu()
        username = input("Enter your username: ")
        if online_mode == 1: # server mode
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((socket.gethostname(), PORT))
                print("Players need to be on the same network to play!")
                print("My IP address: " + s.getsockname()[0])
                print("Waiting for player connection...")
                s.listen()
                conn, addr = s.accept()
                with conn:
                    opponent_name = conn.recv(1024).decode()
                    print(opponent_name + " connected.")
        else: # client mode
            HOST = str(input("Enter the host IP address: "))
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(str.encode(username))

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
