from models.customTypos import Symbol, Position, BoardGrid

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
