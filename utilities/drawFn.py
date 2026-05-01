def drawOnTemplate(arr: list, separation: bool = True):
  """
  DrawOnTemplate recieves an arr part of the
  grid, that would be an array of size 3
  , separation by default is true. 

  Expected result:
    0 | 0 | 0 
  ----+---+----

  Returns:
    bool: True if the list provided is of size 3
  """

  # validation to check if arr meet the requirements
  # by an array of size 3
  if (len(arr) != 3): return False
  
  part = ''
  separator = '-----+-----+-----'

  for i in range(len(arr)):
    end = ''
    if (i < len(arr) - 1): end = '|'
    part += f'  {arr[i]}  {end}'

  print(part)
  if (separation): print(separator)

  return True


# arr: expected recieve a grid of 3x3
def drawBoard(arr: list):
  """
  ⠀⠀⠀|⠀⠀⠀|⠀⠀⠀⠀\n
  ----+----+----\n
  ⠀⠀⠀|⠀⠀⠀|⠀⠀⠀⠀\n
  ----+----+----\n
  ⠀⠀⠀|⠀⠀⠀|⠀⠀⠀⠀\n
  Print the board on terminal\n

  Args: 
    arr (list): A list of size 3 that contains a list of size 3.
  
  Returns:
    bool: True if the print on terminal was successful.
  """


  # Validation for check if arr is 
  # a grid 3x3
  if (len(arr) != 3): return False
  
  for i in range(len(arr)):
    separation = False
    if (i < len(arr)-1): separation = True

    drawOnTemplate(arr[i], separation)

  return True