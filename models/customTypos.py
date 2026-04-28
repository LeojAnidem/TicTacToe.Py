from enum import Enum, IntEnum

class Symbol(Enum):
  X = "X"
  O = "O"

  def __str__(self):
    return str(self.value)

class Status(str, Enum):
  win = 'WIN'
  tie = 'TIE'
  lose = 'LOSE'
  playing = 'PLAYING'

  def __str__(self):
    return str(self.value)

class PosNum(IntEnum):
  ZERO = 0
  ONE = 1
  TWO = 2

type Position = tuple[PosNum, PosNum]
type BoardElement = list[str | Symbol, str | Symbol, str | Symbol]
type BoardGrid = list[BoardElement, BoardElement, BoardElement]