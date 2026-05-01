from utilities.systemFn import cleanScreen
from utilities.drawFn import drawBoard
from utilities.arrFn import createCustomArr
from utilities.checkSimilarities import checkHorizontal
from models.customTypos import Status, Symbol, Position, BoardGrid

VOID = ' '

class Board:
  def __init__(self):
    # Grid is an array of size 3 where each element is 
    # an array of size 3 fill with 0's
    self.grid: BoardGrid = createCustomArr(createCustomArr(VOID , 3), 3)
    
    self.currentMoves = 0
    self.gameStatus:Status = Status.playing
  
  def drawOnScreen(self):
    drawBoard(self.grid)
  
  def updateGrid(self, position: Position, newValue: Symbol):
    if (self.grid[position[0]][position[1]] != VOID): return False
    
    self.grid[position[0]][position[1]] = newValue
    
    cleanScreen()
    self.drawOnScreen()
    self.currentMoves += 1
    
    if (self.currentMoves >= 3):
      if (checkHorizontal(self.grid, position, newValue)):
        self.gameStatus = Status.win

    if (self.currentMoves >= 9):
      for element in self.grid:
        if VOID not in element: 
          self.gameStatus = Status.tie
          return False
    
    return True


  def getData(self):
    return {
      'gameStatus': self.gameStatus,
      'grid': self.grid
    }
  
