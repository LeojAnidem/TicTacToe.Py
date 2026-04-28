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

# Create an array with x value of size n
# x: value  ||  _: accumulator  ||  n: number
# [x for _ in range(n)
def createCustomArr(x, n):
    return [x for _ in range(n)]


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

# Grid is an array of size 3 where each element is 
# an array of size 3 fill with 0's
grid = createCustomArr(createCustomArr(0, 3), 3)
drawBoard(grid)