# Simple-Tic-Tac-Toe
a simple CLI Tic-Tac-Toe game

Overview
This is a basic command-line Tic-Tac-Toe game implemented in Python. It allows two players to play against each other on a 3x3 board.

Features
Interactive Gameplay: Players take turns entering their moves.

Win/Draw Detection: Automatically checks for winning conditions and draws.

Simple Interface: A clear, text-based representation of the game board.

How to Run
Save the code: Save the provided Python code (from tic-tac-toe-python) into a file named tic_tac_toe.py (or any other .py extension).

Open a terminal: Navigate to the directory where you saved the file using your command line or terminal.

Execute the script: Run the game using the Python interpreter:

python tic_tac_toe.py

How to Play
When the game starts, you'll see an empty 3x3 board.

Players will be prompted to enter their move by typing a number from 1 to 9. These numbers correspond to the positions on the board:

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

Player "X" goes first, followed by Player "O".

Enter the number of the empty square where you want to place your mark.

The game will continue until one player gets three of their marks in a row (horizontally, vertically, or diagonally) or all squares are filled, resulting in a draw.

Invalid moves (e.g., choosing an already taken spot or a number out of range) will result in a prompt to try again.

Example Gameplay
Welcome to Tic-Tac-Toe!
Positions are numbered 1-9 from left to right, top to bottom.


   |   |
-----------
   |   |
-----------
   |   |

Player X, enter your move (1-9): 1


 X |   |
-----------
   |   |
-----------
   |   |

Player O, enter your move (1-9): 5


 X |   |
-----------
   | O |
-----------
   |   |

... and so on.
