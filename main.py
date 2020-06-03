
from helpers import Helpers
from random import randint
from socket import *

player_coordinates = {"x": 0, "y": 0}
player1_coordinates = {"x": 0, "y": 0}

board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]

HOST = '127.0.1.1'
PORT = 2911

won = False
first_play = True

game_mode = Helpers.main_menu()
online_mode = 0
s = socket()
conn = "this_will_be_the_server_connection"
username = "Player"
opponent_name = "Opponent"

if game_mode != 0:
    if game_mode == 2: # online mode
        online_mode = Helpers.online_menu()
        username = input("Enter your username: ")
        if online_mode == 1: # server mode
            s.bind((HOST, PORT))
            print("Players need to be on the same network to play!")
            print("My IP address: " + s.getsockname()[0])
            print("Waiting for player connection...")
            s.listen()
            conn, addr = s.accept()
            opponent_name = conn.recv(1024).decode()
            print(opponent_name + " connected.")
            conn.sendall(str.encode(username))
        else: # client mode
            HOST = str(input("Enter the host IP address: "))
            s.connect((HOST, PORT))
            s.sendall(str.encode(username))
            opponent_name = s.recv(1024).decode()
            print("Connected to " + opponent_name + "'s game.")

    must_wait = True
    if online_mode == 1:
        must_wait = False

    while won == False:
        # human (this) plays
        if not must_wait:
            while board[player_coordinates["x"]][player_coordinates["y"]] != 0 or first_play == True:
                raw_coordinates = input("Coordinates (x:y): ")
                player_coordinates["x"] = int(raw_coordinates.split(":")[0]) - 1
                player_coordinates["y"] = int(raw_coordinates.split(":")[1]) - 1
                first_play = False
            board[player_coordinates["x"]][player_coordinates["y"]] = "X"
            if game_mode == 2: # if in online mode, send the play
                if online_mode == 1:
                    conn.send(str(str(player_coordinates["x"]) + ":" + str(player_coordinates["y"])).encode('utf-8'))
                else:
                    s.send(str(str(player_coordinates["x"]) + ":" + str(player_coordinates["y"])).encode('utf-8'))
            won = Helpers.check_win(board)["victory"]
            must_wait = True
        # bot / other player plays
        else:
            if won == False:
                if game_mode == 1:
                    while board[player1_coordinates["x"]][player1_coordinates["y"]] != 0: # generate new coordinates if the space was already filled
                        player1_coordinates["x"] = randint(0, 2)
                        player1_coordinates["y"] = randint(0, 2)
                else: # online mode
                    print("Waiting for the opponent...")
                    raw_coordinates = ""
                    if online_mode == 1: # receive in server mode
                        raw_coordinates = conn.recv(1024).decode('utf-8')
                    else: # receive in client mode
                        raw_coordinates = s.recv(1024).decode('utf-8')
                    print(raw_coordinates)
                    player1_coordinates["x"] = int(raw_coordinates.split(":")[0])
                    player1_coordinates["y"] = int(raw_coordinates.split(":")[1])

                board[player1_coordinates["x"]][player1_coordinates["y"]] = "O"
            must_wait = False

        won = Helpers.check_win(board)["victory"]

        Helpers.show_board(board)

    s.close()

    winner = Helpers.check_win(board)["winner"]
    
    if Helpers.check_win(board)["winner"] == "X":
        winner = username
    elif Helpers.check_win(board)["winner"] == "O":
        winner = opponent_name

    print("WINNER: " + winner)

    Helpers.show_board(board)
