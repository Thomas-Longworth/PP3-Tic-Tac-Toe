# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to eXpect a terminal of 80 characters wide and 24 rows high
import random
import time
import sys

game_grid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
instructions = """Welcome to the this Tic Tac Toe game,
* THe game board is 3x3 grid as shown below,
* The player can play by choosing a number from 0-8,
* A winner is decided when the player or computer gets
three symbols in a row,
* If all 9 grid places are played with no winners it 
will be a draw. 
"""
sample_grid=["0", "1", "2", "3", "4", "5", "6", "7", "8"]


def game_board():

    print("------------------")
    print("  " + game_grid[0] + "  |  " + game_grid[1] + "  |  " + game_grid[2])
    print("  " + game_grid[3] + "  |  " + game_grid[4] + "  |  " + game_grid[5])
    print("  " + game_grid[6] + "  |  " + game_grid[7] + "  |  " + game_grid[8])
    print("------------------")




def game_play ():

    game_board()
    
    
    play1 = int(input("player one enter your number   "))
    if play1 < 0 or play1 > 8:
        print("please choose number between 0 and 8!!!!!!!")
        game_play() 
    

    if (game_grid[play1]=="X" ) or (game_grid[play1]=="O"):
        print("Please Choose a number thats not already been played")
        game_play()


    else:
        game_grid[play1]="X"
        checkP1win()

    game_board()
   
    
    computerPlay()

def computerPlay():

    compPlay = random.randint(0,8)
    
   
    if (game_grid[compPlay]=="X" ) or (game_grid[compPlay]=="O"):
        computerPlay()
    elif game_grid[compPlay]=="-":
        print("Computer playing....")
        time.sleep(0.5)
        print("....")
        time.sleep(0.5)
        print("....")
        time.sleep(0.5)

        game_grid[compPlay]="O"

    
    game_board()
    game_play()


def checkP1win():
    if (game_grid[0] == "X") and (game_grid[1] == "X") and (game_grid[2] == "X"):
        endGameP1()       
    elif (game_grid[3] == "X") and (game_grid[4] == "X") and (game_grid[5]== "X"):
        endGameP1()
    elif (game_grid[6] == "X") and (game_grid[7] == "X") and (game_grid[8] == "X"):
        endGameP1()
    elif (game_grid[0] == "X") and (game_grid[3] == "X") and (game_grid[6]== "X"):
        endGameP1()
    elif (game_grid[1]== "X") and (game_grid[4]== "X") and (game_grid[7]== "X"):
        endGameP1()
    elif (game_grid[2] == "X") and (game_grid[5]== "X") and (game_grid[8]== "X"):
        endGameP1()
    elif (game_grid[0]== "X") and (game_grid[4] == "X") and (game_grid[8] == "X"):
        endGameP1()
    elif (game_grid[2] == "X") and (game_grid[4] == "X") and (game_grid[6] == "X"):
        endGameP1()
    

def checkCompWin():
    if (game_grid[O] == "O") and (game_grid[1] == "O") and (game_grid[2] == "O"):
        end_game_comp()
    if (game_grid[3] == "O") and (game_grid[4] == "O") and (game_grid[5] == "O"):
        end_game_comp()
    if (game_grid[6] == "O") and (game_grid[7]== "O") and (game_grid[8] == "O"):
        end_game_comp()
    if (game_grid[0] == "O") and (game_grid[3] == "O") and (game_grid[6] == "O"):
        end_game_comp()
    if (game_grid[1] == "O") and (game_grid[4] == "O") and (game_grid[7] == "O"):
        end_game_comp()
    if (game_grid[2] == "O") and (game_grid[5] == "O") and (game_grid[8] == "O"):
        end_game_comp()
    if (game_grid[0] == "O") and (game_grid[4] == "O") and (game_grid[8] == "O"):
        end_game_comp()
    if (game_grid[2] == "O") and (game_grid[4] == "O") and (game_grid[6] == "0"):
        end_game_comp()

def end_game_comp():
    print("computer1 win")
    

def endGameP1():
    game_board()
    time.sleep(0.5)
    print("....")
    print("player 1 win")
    time.sleep(0.5)
    print("....")
    print("player 1 win")

    end_input = input("would you like to play again?")
    
   

    reset_game()


def start_program():
    for char in instructions:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(0.5)
    print("------------------")
    print("  " + sample_grid[0] + "  |  " + sample_grid[1] + "  |  " + sample_grid[2])
    print("  " + sample_grid[3] + "  |  " + sample_grid[4] + "  |  " + sample_grid[5])
    print("  " + sample_grid[6] + "  |  " + sample_grid[7] + "  |  " + sample_grid[8])
    print("------------------")

    time.sleep(0.5)

    player_name = input("What is your name?   ")

    user_input= input( f"{player_name}, To play, the game, type the letter 'p' ")
    if user_input.lower()=="p":
        game_play()

    else:
        print("error")



def reset_game():

    game_grid[0]="-"
    game_grid[1]="-"
    game_grid[2]="-"
    game_grid[3]="-"
    game_grid[4]="-"
    game_grid[5]="-"
    game_grid[6]="-"
    game_grid[7]="-"
    game_grid[8]="-"

    
    game_play()





start_program()
