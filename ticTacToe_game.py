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
import os
from utilities.drawFn import drawBoard
from utilities.arrFn import createCustomArr

def cleanScreen():
  os.system('cls' if os.name == 'nt' else 'clear')


class Board:
  def __init__(self):
    # Grid is an array of size 3 where each element is 
    # an array of size 3 fill with 0's
    grid = createCustomArr(createCustomArr(0 , 3), 3)
    self.grid = grid
  
  def drawOnScreen(self):
    drawBoard(self.grid)
  
  def updateGrid(self, position, newValue):
    self.grid[position[0]][position[1]] = newValue
    cleanScreen()
    self.drawOnScreen()

gameBoard = Board()
gameBoard.drawOnScreen()
gameBoard.updateGrid([0,0], 'X')