# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to eXpect a terminal of 80 characters wide and 24 rows high
import random
import time

game_grid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def game_board():

    print("------------------")
    print("  " + game_grid[0] + "  |  " + game_grid[1] + "  |  " + game_grid[2])
    print("  " + game_grid[3] + "  |  " + game_grid[4] + "  |  " + game_grid[5])
    print("  " + game_grid[6] + "  |  " + game_grid[7] + "  |  " + game_grid[8])
    print("------------------")

 
game_board()


    
    



def gamePlay ():
    
    
    play1 = int(input("player one enter your number   "))
    if play1 < 0 or play1 > 8:
        print("please choose number between 0 and 8!!!!!!!")
        gamePlay() 
        

    if (game_grid[play1]=="X" ) or (game_grid[play1]=="O"):
        print("Please Choose a number thats not already been played")
        gamePlay()


    else:
        game_grid[play1]="X"
        checkP1win()
        
        

        

        
    
    

    game_board()
   
    
    computerPlay()

def computerPlay():

    compPlay = random.randint(0,8)

    if (game_grid[compPlay]=="X" ) or (game_grid[compPlay]=="O"):
        computerPlay()
    else:
        print("Computer playing....")
        time.sleep(0.5)
        print("....")
        time.sleep(0.5)
        print("....")
        time.sleep(0.5)
        game_grid[compPlay]="O"
    game_board()
    gamePlay()


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
    if (game_grid[O] == "O") and (game_grid[0] == "O") and (game_grid[0] == "O"):
        endGameP2()
    if (game_grid[1] == "O") and (game_grid[1] == "O") and (game_grid[1] == "O"):
        endGameP2()
    if (game_grid[2] == "O") and (game_grid[2]== "O") and (game_grid[2] == "O"):
        endGameP2()
    if (game_grid[0] == "O") and (game_grid[1] == "O") and (game_grid[2] == "O"):
        endGameP2()
    if (game_grid[0] == "O") and (game_grid[1] == "O") and (game_grid[2] == "O"):
        endGameP2()
    if (game_grid[0] == "O") and (game_grid[1] == "O") and (game_grid[2] == "O"):
        endGameP2()
    if (game_grid[0] == "O") and (game_grid[1] == "O") and (game_grid[2] == "O"):
        endGameP2()
    if (game_grid[0][2] == "O") and (game_grid[1][1] == "O") and (game_grid[0][2] == "0"):
        endGameP2()




def endGameP2():
    print("computer1 win")

def endGameP1():
    time.sleep(0.5)
    print("....")
    print("player 1 win")
    time.sleep(0.5)
    print("....")
    print("player 1 win")

    

gamePlay()


