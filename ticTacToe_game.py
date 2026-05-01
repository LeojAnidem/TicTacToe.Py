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
from models.PlayerClass import Player
from models.customTypos import Symbol, Status, Position
from models.BoardClass import Board
from models.scoreboardClass import Scoreboard
from utilities.systemFn import cleanScreen
from utilities.arrFn import forceExpectedAnswer

# Initialize
gameBoard:Board = Board()
score:Scoreboard = Scoreboard()

# Defining player symbol
userInput = ''
secondSymbol = ''
while (type(userInput) != Symbol):
  cleanScreen()
  userInput = str(input(f'[PLAYER #1] Select X or O as symbol: ')).upper()
  if userInput == 'X': 
    userInput = Symbol.X
    secondSymbol = Symbol.O
  if userInput == 'O': 
    userInput = Symbol.O
    secondSymbol = Symbol.X


# A list with player data
players = [Player(userInput), Player(secondSymbol)]

# Start bucle for the game
stillPlaying = True
while (stillPlaying):

  # Player turn
  currentTurn = 0
  while ((currentTurn < 1 ) or (currentTurn > 2)):
    cleanScreen()
    currentTurn = int(input('Select who start first[1 OR 2] : '))

  # Draw the board
  cleanScreen()
  # gameBoard.testWin() # Testing Function
  # gameBoard.testTie() # Testing Function
  gameBoard.drawOnScreen()
  print('\n')

  while(gameBoard.gameStatus == Status.playing):
    position:Position = []
    print(f'[SYSTEM]: CURRENT TURN -> PLAYER #{currentTurn} ( {players[currentTurn-1].getSymbol()} )')

    # Request position to current player
    for i in range(2):
      namePos = 'Row' if i == 0 else 'Column' 

      posInput = -1
      while (posInput < 0 or posInput > 2):
        posInput = int(input(f'[Player# {currentTurn}] Select {namePos} position by writen an number [0,1,2]: '))
      
      position.append(posInput)

    # Summit position to grid and check is a valid position
    isValidPos = gameBoard.updateGrid(position, players[currentTurn-1].getSymbol())

    # If is not a valid position, clean the screen and start bucle again
    if not isValidPos:
      cleanScreen()
      gameBoard.drawOnScreen()
      print('[SYSTEM]: INVALID MOVEMENT, A PLAYER HAS ALREADY TAKE THAT POSITION')
      continue

    if (gameBoard.gameStatus != Status.playing):
      player: Player 

      print('\n')

      if (gameBoard.gameStatus == Status.tie):
        for player in players: player.updateData()
        print(f"[SYSTEM]: Nobody Wins, It's a Draw!")
        currentTurn = 0
        break

      for i, player in enumerate(players): 
        isWinner = True if (i == currentTurn - 1) else False
        player.updateData(isWinner)

      print(f'[SYSTEM]: Player# {currentTurn} ({players[currentTurn-1].getSymbol()}) Wins!')
      break
        
    # If all ok, pass turn to next player
    currentTurn = 2 if currentTurn == 1 else 1

  # TODO: Refactor. Get Players as parameter and susbstract games played and wins.
  score.updateScoreboard(currentTurn)


  val = forceExpectedAnswer('Do you want play agin? (Y/N)', ['Y', 'N'])
  stillPlaying = True if (val == 'Y') else False

  gameBoard.reset()
