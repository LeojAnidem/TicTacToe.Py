from utilities.systemFn import cleanScreen
from utilities.drawFn import drawBoard
from utilities.arrFn import createCustomArr

class Board:
  def __init__(self):
    # Grid is an array of size 3 where each element is 
    # an array of size 3 fill with 0's
    grid = createCustomArr(createCustomArr(' ' , 3), 3)
    self.grid = grid
  
  def drawOnScreen(self):
    drawBoard(self.grid)
  
  def updateGrid(self, position, newValue):
    self.grid[position[0]][position[1]] = newValue
    cleanScreen()
    self.drawOnScreen()