# tic_tac_toe #

An interactive code that allows 2 people to play this game.

# Steps in writing the code #

Step 1: Getting started
Let's start with the main structure, which will start our game when you run the script name in the command line. 

Since a game of Tic-tac-toe is basically repeating the same tasks over and over again (like asking the players for input) a while True loop helped to get the game running. We have to make sure, however, that in case of certain events (win, draw,...) the loop will break so that the game will come to an end. Another challenge to think about was how to allow each player to take turns at making their moves.

Step 2: Display the board
To play a round of tic-tac-toe, we need a game board. We should start by defining a function that will display the board on the screen when it is called. There are several ways to display a tic-tac-toe board. We have chosen the implementation as below:

1, 2, 3
4, 5, 6
7, 8, 9

Step 3: Choose a symbol
Before we can start playing it would be nice if the first player can choose whether to play with "X" or "O"! Player two must then choose the other.

Step 4: Ask for player input
Now we need a function that asks the player (whose turn it is) where he wants to put his marker. The built-in function input() will do this task.  The code checks if the desired position was already occupied in a previous turn.

Step 5: Check for Winner
At the end of each turn, our script will have to determine if the most recent play resulted in a win. If it did, it should break the game loop, the player that just played will be declared the winner, the game will be over, and the script will terminate. If a winner is not found, play will continue. There are 8 different ways for a player to get three in a row.

Step 6: Check for Draw
There is a distinct chance that a draw will occur in the game. If this happens, script should be aware. If all of the squares have been filled in, and there is no winner, it should break the game loop and a draw should be declared.

# Extras #

Play the game for several times back to back without breaking
