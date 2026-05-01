from models.customTypos import PosNum

class Scoreboard:
  def __init__(self):
    self.gamesPlayed = 0
    self.player1Wins = 0
    self.player2Wins = 0
  
  def getData(self):
    return self.__dict__

  def updateScoreboard(self, numPlayerWin: PosNum):
    if (numPlayerWin < 0 or numPlayerWin > 2):
      print('[SYSTEM]: Error, player not found!')
      return False
    
    if numPlayerWin == 1: self.player1Wins += 1
    if numPlayerWin == 2: self.player2Wins += 1
    
    self.gamesPlayed += 1
    self.drawOnScreen()
    return True
  
  def drawOnScreen(self):
    """
    +------------------------------+\n
    | Games Played: 00             |\n
    +------------------------------+\n
    |⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀WINS⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|\n
    +---------------+--------------+\n
    |⠀⠀⠀PLAYER#1⠀⠀⠀|⠀⠀⠀PLAYER#2⠀⠀⠀|\n
    +---------------+--------------+\n
    |⠀⠀⠀⠀⠀⠀00⠀⠀⠀⠀⠀⠀|⠀⠀⠀⠀⠀⠀00⠀⠀⠀⠀⠀⠀|\n
    +---------------+--------------+\n

    Print the scoreBoard on terminal\n

    ARGS: 
      scoreboard (dict): Recieves an element dict of type Scoreboard
    
    Returns: 
      bool: True if the print on terminal was succesful
    """

    s = '+------------------------------+'
    sS = '+---------------+--------------+'
    games = f'| Games Played: {self.gamesPlayed}              |'
    title = '|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀WINS⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|'
    modelBase = [s, games, s, title]

    part = '|⠀'
    scorePart = '|⠀'
    for indexPlayer in range(2):
      part += f'⠀⠀⠀PLAYER#{indexPlayer + 1}⠀⠀⠀|'
      scorePlayer = self.player1Wins if indexPlayer == 0 else self.player2Wins
      scorePart += f'⠀⠀⠀⠀⠀⠀⠀{scorePlayer}⠀⠀⠀⠀⠀⠀|'

    for i in range(2):
      modelBase.append(sS)
      currentPart = part if (i == 0) else scorePart
      modelBase.append(currentPart)

    modelBase.append(sS)

    for ePart in modelBase: print(ePart)

    return True