
import random
import time
import sys

#This is the grid list for the game
game_grid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

#These are variables for keeping the scores of the game
computer_score=0
player_score = 0


#Instructions for plaing the game
instructions = """Welcome to the this Tic Tac Toe game,
* The game board is 3x3 grid as shown below,
* The player can play by choosing a number from 0-8,
* A winner is decided when the player or computer gets
three symbols in a row,
* If all 9 grid places are played with no winners it, 
will be a draw. 
"""
sample_grid=["0", "1", "2", "3", "4", "5", "6", "7", "8"]

#Function for displaying the game board
def game_board():
    print("------------------")
    print("  " + game_grid[0] + "  |  " + game_grid[1] + "  |  " + game_grid[2])
    print("  " + game_grid[3] + "  |  " + game_grid[4] + "  |  " + game_grid[5])
    print("  " + game_grid[6] + "  |  " + game_grid[7] + "  |  " + game_grid[8])
    print("------------------")

#This is the function for the main gameplay loop
def game_play ():
    game_board()
    play_1 = int(input("Please enter your number 0-8   "))

    if play_1 < 0 or play_1 > 8:
        print("please choose number between 0 and 8!!!!!!!")
        game_play() 
    if (game_grid[play_1]=="X" ) or (game_grid[play_1]=="O"):
        print("Please Choose a number thats not already been played")
        game_play()
    else:
        game_grid[play_1]="X"
        time.sleep(0.5)
        check_player_win()
    game_board()
    computer_play()

#Function for the computer to play on the board
def computer_play():
    compPlay = random.randint(0,8)

    if (game_grid[compPlay]=="X") or (game_grid[compPlay]=="O"):
        computer_play()
    elif game_grid[compPlay]=="-":
        print("Computer playing....")
        time.sleep(0.5)
        print("....")
        time.sleep(0.5)
        print("....")
        time.sleep(0.5)

        game_grid[compPlay]="O"
        check_comp_win()

    game_play()

#This function checks if the player has won the game.
def check_player_win():
    if (game_grid[0] == "X") and (game_grid[1] == "X") and (game_grid[2] == "X"):
        end_game_player()       
    elif (game_grid[3] == "X") and (game_grid[4] == "X") and (game_grid[5]== "X"):
        end_game_player()   
    elif (game_grid[6] == "X") and (game_grid[7] == "X") and (game_grid[8] == "X"):
        end_game_player()   
    elif (game_grid[0] == "X") and (game_grid[3] == "X") and (game_grid[6]== "X"):
        end_game_player()   
    elif (game_grid[1]== "X") and (game_grid[4]== "X") and (game_grid[7]== "X"):
        end_game_player()   
    elif (game_grid[2] == "X") and (game_grid[5]== "X") and (game_grid[8]== "X"):
        end_game_player()   
    elif (game_grid[0]== "X") and (game_grid[4] == "X") and (game_grid[8] == "X"):
        end_game_player()   
    elif (game_grid[2] == "X") and (game_grid[4] == "X") and (game_grid[6] == "X"):
        end_game_player()   
    
#This function checks if the computer has won the game
def check_comp_win():
    if (game_grid[0] == "O") and (game_grid[1] == "O") and (game_grid[2] == "O"):
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
    if (game_grid[2] == "O") and (game_grid[4] == "O") and (game_grid[6] == "O"):
        end_game_comp()

#This function executes when the computer has won a game
def end_game_comp():
    global computer_score
    game_board()
    computer_score +=1

    time.sleep(0.5)
    print("....")
    print("The computer wins")
    time.sleep(1)
    print("Calulating scores")
    print("....")
    time.sleep(0.5)
    print("--------------------------------------")
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    print("--------------------------------------")

    input_reset= input("To play the game again, type the letter 'p' \n ")
    if input_reset.lower()=="p":
        reset_game()

#This function executes when the Player has won a game
def end_game_player()   :
    global player_score
    game_board()
    player_score +=1

    time.sleep(0.5)
    print("....")
    print("Player wins")
    time.sleep(1)
    print("Calulating scores")
    time.sleep(0.5)
    print("....")
    print("--------------------------------------")
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    print("--------------------------------------")
    
    input_reset = input("To play the game again, type the letter 'p' \n ")
    if input_reset.lower()=="p":
        reset_game()

#This is the initial function for starting the game
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
    user_input= input( f"{player_name}, To play the game, type the letter 'p' \n ")
    if user_input.lower()=="p":
        game_play()
    else:
        print("error")

#This function restarts the game
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
