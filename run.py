# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


game_grid = [["_", "_", "_"], ["_", "_", "_"],["_", "_", "_"]]

def game_board():
    count = 0
    print("    0    1    2")
    for row in game_grid:
        print(count, row)
        count = count + 1
    
game_board()



def endGameP1():
    print("Player 1 has won the game")

def check_win():
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




def gamePlay ():
    
    play1row = int(input("player one enter your row number   "))
    play1col = int(input("player one enter column number     "))
    game_grid[play1row][play1col]='x'

    game_board()
    check_win()

    play2row = int(input("player 2 enter your row number   "))
    play2col = int(input("player 2 enter column number     "))
    game_grid[play2row][play2col]="0"

    game_board()
    check_win()
    gamePlay()

gamePlay()


