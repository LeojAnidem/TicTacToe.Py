from models.customTypos import Symbol

class Player:
  def __init__(self, symbol: Symbol):
    self.symbol = symbol
    self.wins = 0
    self.gamesPlayed = 0
    self.losses = 0
    self.isWinner = False

  def updateData(self, isAWin: bool):
    self.gamesPlayed += 1
    if isAWin: 
      self.wins += 1
      self.isWinner = True
    else: self.losses += 1 

  def getData(self):
    return {
      'Wins': self.wins,
      "loses": self.losses,
      "gamesPlayed": self.gamesPlayed,
      "symbol": self.symbol
    }
  
  def getSymbol(self):
    return self.symbol