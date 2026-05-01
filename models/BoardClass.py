from utilities.systemFn import cleanScreen
from utilities.drawFn import drawBoard
from utilities.arrFn import createCustomArr, deepCopy
from utilities.checkSimilarities import checkHorizontal
from models.customTypos import Status, Symbol, Position, BoardGrid

VOID = ' '
GRID_DEFAULT = createCustomArr(createCustomArr(VOID , 3), 3)

class Board:
  def __init__(self):
    # Grid is an array of size 3 where each element is 
    # an array of size 3 fill with 0's
    self.grid: BoardGrid = deepCopy(GRID_DEFAULT)
    
    self.currentMoves = 0
    self.gameStatus:Status = Status.playing
  
  def drawOnScreen(self):
    drawBoard(self.grid)

  def reset(self):
    self.grid = deepCopy(GRID_DEFAULT)
    self.gameStatus = Status.playing
  
  def updateGrid(self, position: Position, newValue: Symbol):
    if (self.grid[position[0]][position[1]] != VOID): return False
    
    self.grid[position[0]][position[1]] = newValue
    
    cleanScreen()
    self.drawOnScreen()
    self.currentMoves += 1
    
    if (self.currentMoves >= 3):
      if (checkHorizontal(self.grid, position, newValue)):
        self.gameStatus = Status.win

    if (self.currentMoves >= 9 and self.gameStatus == Status.playing):
      for element in self.grid:
        if VOID not in element: 
          self.gameStatus = Status.tie
    
    return True
    
  def testTie(self):
    self.grid = [
      [Symbol.X,Symbol.X, Symbol.O],
      [Symbol.O,Symbol.O, Symbol.X,],
      [Symbol.X, Symbol.O, VOID]
    ]

    self.currentMoves = 8
    
  def testWin(self):
    self.grid = [
      [Symbol.X,Symbol.X, Symbol.X],
      [Symbol.O,Symbol.O, Symbol.X,],
      [Symbol.O, Symbol.O, VOID]
    ]

    self.currentMoves = 8
    

