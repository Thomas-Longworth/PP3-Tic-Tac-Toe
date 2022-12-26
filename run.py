# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


game_grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def game_board():

    print(game_grid[0:3])
    print(game_grid[3:6])
    print(game_grid[6:9])

    
    
game_board()



def endGameP1():
    print("Player 1 has won the game")

def endGameP2():
    print("Player 2 has won the game")

def check_win_p1():
    if (game_grid[0][0] == "x") and (game_grid[0][1] == "x") and (game_grid[0][2] == "x"):
        endGameP1()
    if (game_grid[1][0] == "x") and (game_grid[1][1] == "x") and (game_grid[1][2] == "x"):
        endGameP1()
    if (game_grid[2][0] == "x") and (game_grid[2][1] == "x") and (game_grid[2][2] == "x"):
        endGameP1()
    if (game_grid[0][0] == "x") and (game_grid[1][0] == "x") and (game_grid[2][0] == "x"):
        endGameP1()
    if (game_grid[0][1] == "x") and (game_grid[1][1] == "x") and (game_grid[2][1] == "x"):
        endGameP1()
    if (game_grid[0][2] == "x") and (game_grid[1][2] == "x") and (game_grid[2][2] == "x"):
        endGameP1()
    if (game_grid[0][0] == "x") and (game_grid[1][1] == "x") and (game_grid[2][2] == "x"):
        endGameP1()
    if (game_grid[0][2] == "x") and (game_grid[1][1] == "x") and (game_grid[0][2] == "x"):
        endGameP1()

def check_win_p2():
    if (game_grid[0][0] == "0") and (game_grid[0][1] == "0") and (game_grid[0][2] == "0"):
        endGameP2()
    if (game_grid[1][0] == "0") and (game_grid[1][1] == "0") and (game_grid[1][2] == "0"):
        endGameP2()
    if (game_grid[2][0] == "0") and (game_grid[2][1] == "0") and (game_grid[2][2] == "0"):
        endGameP2()
    if (game_grid[0][0] == "0") and (game_grid[1][0] == "0") and (game_grid[2][0] == "0"):
        endGameP2()
    if (game_grid[0][1] == "0") and (game_grid[1][1] == "0") and (game_grid[2][1] == "0"):
        endGameP2()
    if (game_grid[0][2] == "0") and (game_grid[1][2] == "0") and (game_grid[2][2] == "0"):
        endGameP2()
    if (game_grid[0][0] == "0") and (game_grid[1][1] == "0") and (game_grid[2][2] == "0"):
        endGameP2()
    if (game_grid[0][2] == "0") and (game_grid[1][1] == "0") and (game_grid[0][2] == "0"):
        endGameP2()


def gamePlay ():
    
    play1 = int(input("player one enter your number   "))
    
    game_grid[play1]='x'

    game_board()
    check_win_p1()

    play2 = int(input("player 2 enter your number   "))
    
    game_grid[play2]="0"

    game_board()
    check_win_p2()
    gamePlay()

gamePlay()


