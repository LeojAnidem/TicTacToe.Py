'''
--------------------
|   Tic-Tac-Toe    |
--------------------
Jeremy Medina (leoj_anidem)
CST 1101

Requirements:
------------------------------
Board Setup: Create and maintain a 3 times 3 grid using an appropriate data structure ( 2D list).
Visual Representation: Implement a function to print the current state of the board to the console after every turn.
Player Setup: Assign specific markers (e.g., 'X' and 'O') to two players and track whose turn it is. 
'''

# IMPORTS
from models.PlayerClass import Player
from models.customTypos import Symbol
from models.BoardClass import Board

player1 = Player(Symbol.X)
player2 = Player(Symbol.O)

gameBoard:Board = Board()
gameBoard.drawOnScreen()
gameBoard.updateGrid([0,0], player1.getSymbol())
gameBoard.updateGrid([1,1], player2.getSymbol())
gameBoard.updateGrid([0,1], player1.getSymbol())
gameBoard.updateGrid([1,2], player1.getSymbol())

print(player1.getData())
