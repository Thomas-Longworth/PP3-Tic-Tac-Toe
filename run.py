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