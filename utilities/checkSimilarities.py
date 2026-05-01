from models.customTypos import Symbol, Position, BoardGrid

def checkDiagonal(arr: BoardGrid, lastPosition: Position, symbol: Symbol):
  # List that store possible corner that meet win's condition
  cornerPositionTocheck: list[Position, Position, Position] = []
  
  # Down diagonal
  # Pick all positions where coordinates are the same
  if (lastPosition[0] == lastPosition[1]):
    for i in range(len(arr)):
      for j in range(len(arr)):
          if (i == j): cornerPositionTocheck.append([i, j])
  
  # Up diagonal
  # Pick all position that meet condition of be in opposites corners
  # and center (1,1)
  elif (lastPosition[0] == (len(arr)-1) or lastPosition[1] == (len(arr)-1)):
    for i in range(len(arr)):
      for j in range(len(arr)):
        cond1 = i == (len(arr)-1) and j == 0
        cond2 = i == 0 and j == (len(arr)-1)

        if (cond1 or cond2):
          cornerPositionTocheck.append([i, j])
      
    cornerPositionTocheck.append([1,1])

  # Check every position store to verified if all had the same symbol
  for x, y in cornerPositionTocheck:
    symbolInPos = arr[x][y]
    if symbol != symbolInPos:
      return False
  
  # Additional verification. In case that length of store possible position
  # is different from length of grid, return false
  if (len(cornerPositionTocheck) != len(arr)): return False

  return True


def checkAxis(arr: BoardGrid, lastPosition: Position, symbol: Symbol):
  # Determine if position correspond to top, center or bottom
  horizontal = True,
  vertical = True

  # axisIndes represent index of the position (x or y) in lastPosition
  for axisIndex in range(len(lastPosition)):
    axisPositionTocheck: Position = []
    
    # In each bucle we check posibilities for x or y (when axisIndex == 0: x. Else: y)
    # If x or y == 0, we check position in same row or col by adding 1 and 2 (x/y = 0, returns [1, 2])
    if (lastPosition[axisIndex] == 0):
      axisPositionTocheck = [lastPosition[axisIndex] + 1, lastPosition[axisIndex] + 2]

    # If x or y == 1, we check position in same row or col by adding 1 and substracting 1 (x/y = 1, returns [2, 0])
    elif (lastPosition[axisIndex] == 1):
      axisPositionTocheck = [lastPosition[axisIndex] + 1, lastPosition[axisIndex] - 1]

    # If x or y == 2, we check position in same row or col by substracting 1 and substracting 2 (x/y = 2, returns [1, 0])
    else:
      axisPositionTocheck = [lastPosition[axisIndex] - 1, lastPosition[axisIndex] - 2]

    # When we have the possible positions, check each of them and compare to see if they have the same symbol
    # Example (x=2; [1,0]) -> axis represents 1 and 0
    for axis in axisPositionTocheck:
      # check all axis in same col and row of lastPosition
      # if axisIndex == 0 check horizontal, else check vertical
      symbolInPos = arr[axis][lastPosition[1]] if (axisIndex == 0) else arr[lastPosition[0]][axis]

      if symbol != symbolInPos:
        if (axisIndex == 0):  horizontal = False
        else: vertical = False

  # No same symbol in horizontal and vertical return false. Win condition dont meet
  if (not horizontal and not vertical): return False

  # Horizontal or vertical have same symbol. Win condition meet
  return True