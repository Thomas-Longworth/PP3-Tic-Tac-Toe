import random
import time
import sys

# This is the grid list for the game
game_grid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# These are variables for keeping the scores of the game
computer_score = 0
player_score = 0


# Instructions for playing the game
instructions = """Welcome to the this Tic Tac Toe game,
* The game board is 3x3 grid as shown below,
* The player can play by choosing a number from 0-8,
* A winner is decided when the player or computer gets
three symbols in a row,
* If all 9 grid places are played with no winners it,
will be a draw.
"""
sample_grid = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

# Function for displaying the game board


def game_board():
    print("------------------")
    print("  " + game_grid[0] + "  |  " + game_grid[1] + "  |  " + game_grid[2])
    print("  " + game_grid[3] + "  |  " + game_grid[4] + "  |  " + game_grid[5])
    print("  " + game_grid[6] + "  |  " + game_grid[7] + "  |  " + game_grid[8])
    print("------------------")

# This is the function for the main gameplay loop


def game_play():
    game_board()
    try:
        play_1 = int(input("Please enter your number 0-8   "))
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 8.")
        game_play()

    if play_1 < 0 or play_1 > 8:
        print("please choose number between 0 and 8!!!!!!!")
        game_play()
    elif (game_grid[play_1] == "X") or (game_grid[play_1] == "O"):
        print("Please Choose a number thats not already been played")
        game_play()
    else:
        game_grid[play_1] = "X"
        time.sleep(0.5)
        check_player_win()
    game_board()
    computer_play()

# Function for the computer to play on the board


def computer_play():
    compPlay = random.randint(0, 8)
    if (game_grid[compPlay] == "X") or (game_grid[compPlay] == "O"):
        computer_play()
    elif game_grid[compPlay] == "-":
        print("Computer playing....")
        time.sleep(0.5)
        print("....")
        time.sleep(0.5)
        print("....")
        time.sleep(0.5)

        game_grid[compPlay] = "O"
        check_comp_win()

    game_play()

# This function checks if the player has won the game.


def check_player_win():
    if (game_grid[0] == "X") and (game_grid[1] == "X") and (game_grid[2] == "X"):
        end_game_player()
    elif (game_grid[3] == "X") and (game_grid[4] == "X") and (game_grid[5] == "X"):
        end_game_player()
    elif (game_grid[6] == "X") and (game_grid[7] == "X") and (game_grid[8] == "X"):
        end_game_player()
    elif (game_grid[0] == "X") and (game_grid[3] == "X") and (game_grid[6] == "X"):
        end_game_player()
    elif (game_grid[1] == "X") and (game_grid[4] == "X") and (game_grid[7] == "X"):
        end_game_player()
    elif (game_grid[2] == "X") and (game_grid[5] == "X") and (game_grid[8] == "X"):
        end_game_player()
    elif (game_grid[0] == "X") and (game_grid[4] == "X") and (game_grid[8] == "X"):
        end_game_player()
    elif (game_grid[2] == "X") and (game_grid[4] == "X") and (game_grid[6] == "X"):
        end_game_player()

    check_draw()
# This is the function to check if game is draw


def check_draw():

    if all(elem == "X" or elem == "O" for elem in game_grid):
        end_game_draw()
    else:
        computer_play()
# This function checks if the computer has won the game


def check_comp_win():
    if (game_grid[0] == "O") and (game_grid[1] == "O") and (game_grid[2] == "O"):
        end_game_comp()
    if (game_grid[3] == "O") and (game_grid[4] == "O") and (game_grid[5] == "O"):
        end_game_comp()
    if (game_grid[6] == "O") and (game_grid[7] == "O") and (game_grid[8] == "O"):
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

# This function executes when the computer has won a game


def end_game_comp():
    global computer_score
    game_board()
    computer_score += 1

    time.sleep(0.5)
    print("....")
    print("The computer wins")
    time.sleep(1)
    print("Calulating scores")
    print("....")
    time.sleep(0.5)
    print("--------------------------------------")
    print(f"Human Score: {player_score}")
    print(f"Computer score: {computer_score}")
    print("--------------------------------------")
    time.sleep(0.5)
    print("Type the letter p to play agin")

    while True:

        input_reset = input().strip().lower()
        if input_reset == "p":
            reset_game()
        else:
            print("Wrong input, please use the letter p")

# This function executes when the Player has won a game


def end_game_player():
    global player_score
    game_board()
    player_score += 1

    time.sleep(0.5)
    print("....")
    print("Player wins")
    time.sleep(1)
    print("Calulating scores")
    time.sleep(0.5)
    print("....")
    print("--------------------------------------")
    print(f"Human score : {player_score}")
    print(f"Computer score: {computer_score}")
    print("--------------------------------------")
    print("   ")
    time.sleep(0.5)
    print("Type the letter p to play agin")

    while True:

        input_reset = input().strip().lower()
        if input_reset == "p":
            reset_game()
        else:
            print("Wrong input, please use the letter p")

# Function to end the game as draw


def end_game_draw():
    global computer_score
    global player_score
    game_board()
    computer_score += 1
    player_score += 1
    time.sleep(0.5)
    print("....")
    print("Its a draw!!")
    time.sleep(1)
    print("Calulating scores")
    print("....")
    time.sleep(0.5)
    print("--------------------------------------")
    print(f"Human score: {player_score}")
    print(f"Computer score: {computer_score}")
    print("--------------------------------------")

    time.sleep(0.5)
    print("Type the letter p to play agin")

    while True:

        input_reset = input().strip().lower()
        if input_reset == "p":
            reset_game()
        else:
            print("Wrong input, please use the letter p")

# This is the initial function for starting the game


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
    print(f"{player_name}, Type the letter s to start the game")
    while True:
        user_start_input = input().strip().lower()
        if user_start_input == "s":
            game_play()
        else:
            print("Wrong input, please use the letter s")

# This function restarts the game


def reset_game():
    game_grid[0] = "-"
    game_grid[1] = "-"
    game_grid[2] = "-"
    game_grid[3] = "-"
    game_grid[4] = "-"
    game_grid[5] = "-"
    game_grid[6] = "-"
    game_grid[7] = "-"
    game_grid[8] = "-"

    game_play()


start_program()
