'''
DrawOnTemplate recieves an arr part of the
grid, that would be an array of size 3
, separation by default is true. 

Expected result:
  0 | 0 | 0 '
----+---+----
'''
def drawOnTemplate(arr, separation = True):
  # validation to check if arr meet the requirements
  # by an array of size 3
  if (len(arr) != 3): return False
  
  part = ''
  separator = '----+----+----'

  for i in range(len(arr)):
    end = ''
    if (i < len(arr) - 1): end = '|'
    part += f' {arr[i]}  {end}'

  print(part)
  if (separation): print(separator)

  return True

# Draw the board
'''
    |   |   
----+---+----
    |   |   
----+---+----
    |   |   
'''
# arr: expected recieve a grid of 3x3
def drawBoard(arr):
  # Validation for check if arr is 
  # a grid 3x3
  if (len(arr) != 3): return False
  
  for i in range(len(arr)):
    if len(arr[i]) != 3: return False
    
    separation = False
    if (i < len(arr)-1): separation = True

    drawOnTemplate(arr[i], separation)
