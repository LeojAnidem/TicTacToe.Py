from utilities.systemFn import cleanScreen
from utilities.drawFn import drawBoard
from utilities.arrFn import createCustomArr
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
    if (self.grid[position[0]][position[1]] != VOID):
      print('[SYSTEM]: INVALID MOVEMENT, A PLAYER HAS ALREADY TAKE THAT POSITION')
      return False
    
    self.grid[position[0]][position[1]] = newValue
    
    cleanScreen()
    self.drawOnScreen()
    self.currentMoves += 1
    
    if (self.currentMoves >= 3):
      print(checkHorizontal(self.grid, position, newValue))
      return


  def getData(self):
    return {
      'gameStatus': self.gameStatus,
      'grid': self.grid
    }
  

def checkHorizontal(arr: BoardGrid, lastPosition: Position, symbol: Symbol):
  # Determine if position correspond to top, center or bottom
  yPositionTocheck: Position = []
  
  if (lastPosition[1] == 1):
    yPositionTocheck = [lastPosition[1] + 1, lastPosition[1] - 1]
  elif (lastPosition[1] == 0):
    yPositionTocheck = [lastPosition[1] + 1, lastPosition[1] + 2]
  else:
    yPositionTocheck = [lastPosition[1] - 1, lastPosition[1] - 2]

  for y in yPositionTocheck:
    if symbol != arr[lastPosition[0]][y]: return False
  
  return True
