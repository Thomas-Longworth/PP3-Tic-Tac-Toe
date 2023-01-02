# Tic Tac Toe Game

![Main](images/res.JPG)




## How to play


* The game board is 3x3 grid as shown below,
* The player can play by choosing a number from 0-8,
* A winner is decided when the player or computer gets
three symbols in a row. This can be horizontally, vertically or diagnoal
* If all 9 grid places are played with no winners it,
will be a draw.

![game](images/game-board.JPG)


## Features 

### Computer
The player plays against the computer. 
The computer generates a random number between 1 and 8 to play.

### Score keeping
After the player or computer wins, the number of wins is recorded and displayed.
### Reset game
The player can reset the game and play again



## Testing
I have tested the game with the following:

- It passed through CI Python Linter with no major issues.
- I tested it in the vscode terminal and on Heroku
- I tried playing invalid grid numbers and inputs while playing the game


# Bugs 
## Solved bugs
- I had an issue with some functions not being able to change variables that were declared somewhere else.
However I fixed this with global keyword in the function.

## Unsolved bugs 
- I was trying to figure out a way to declare the game a draw but I ran out of time to solve this problem.
- When the player doesnt play an interger, the program crashes


# Deployment 

- Sign up/ login to heroku.

- Click on Create App

- Link Heroku app to repository on github.

- Click Deploy.







## Credits

#### Content
- For the Python, I got some ideas from Sentdex on Youtube

#### Deployent
-Code institute for the terminal

