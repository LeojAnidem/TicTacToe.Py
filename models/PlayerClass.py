from models.customTypos import Symbol

class Player:
  def __init__(self, symbol: Symbol):
    self.symbol = symbol
    self.wins = 0
    self.gamesPlayed = 0

  def updateData(self, isAWin: bool = False):
    self.gamesPlayed += 1
    if isAWin: self.wins += 1

  def getData(self):
    return {
      'Wins': self.wins,
      "gamesPlayed": self.gamesPlayed,
      "symbol": self.symbol
    }
  
  def getSymbol(self):
    return self.symbol