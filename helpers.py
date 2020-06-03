
class Helpers:

    def main_menu():
        opt = -1
        while opt < 0 or opt > 2:
            print("** TIC TAC TOE**\n")
            print("1. Player vs Computer")
            print("2. Player vs Player")
            print("0. Exit\n")
            opt = int(input("Select an option: "))
        return opt
    
    def show_board(board):

        print("")
        
        for i in range(0, 3): # each row
            for j in range(0, 3): # each col
                if board[i][j] != 0: # a value was set
                    print(board[i][j], end="")
                else:
                    print(" ", end="")
                if j < 2: # vertical lines
                    print(" | ", end="")
            if i < 2:
                print("\n- - - - -")

        print("\n")

    def check_win(board):

        return_value = {"victory": False, "winner": None}

        for x in range(0,3):
            if board[x][0] == board[x][1] == board[x][2] and board[x][0] != 0:
                return_value["victory"] = True
                return_value["winner"] = board[x][0]

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
            return_value["victory"] = True
            return_value["winner"] = board[0][0]

        elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
            return_value["victory"] = True
            return_value["winner"] = board[0][2]

        count = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] != 0:
                    count += 1

        if return_value["victory"] == False and count == 9: # all spaces are filled and there is no winner, so it's a draft
            return_value["victory"] = True
            return_value["winner"] = "Draft"

        
        return return_value
