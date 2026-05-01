def createCustomArr(x: any, n: int):
  """
  Create a list with x value of size n

  Args:
    x (any): String, Int or List value
    n (int): The size of array

  Returns:
    list: A list fill with x values of size n
  """
  return [x[:] if isinstance(x, list) else x for _ in range(n)]


def deepCopy(arr: list):
  """
  Create a copy of a list without reference

  Args:
    arr (list): List with/o other lists inside

  Returns:
    List: A exact copy of the original but with new address in memory.
  """
  return [
    deepCopy(e) if isinstance(e, list) else e for e in arr
  ]


def forceExpectedAnswer(message: str, expectedAnswer: list[str | int, str | int]) -> str | int:
  """
  Create a bucle that ends when user insert the one of the expected answers

  Args:
    message (str): Dev or system message to the user. Ex. Write a number between 1 and 5.
    expectedAnswer (list): A list of deseables answers. Ex. [1,2,3,4,5]

  Returns:
    str | int : Return one value of the expected answers.
  """
  inptUsr = ''
  stillAsking = True

  while (stillAsking):
    inptUsr = (str if (type(expectedAnswer[0]) == str) else int)(input(f'[SYSTEM]: {message}: ').upper())
    
    altCondition = inptUsr not in [element.upper() for element in expectedAnswer]
    condition = inptUsr not in expectedAnswer 
    stillAsking = condition if (type(expectedAnswer[0]) == int) else altCondition
    
    if (stillAsking): print (f'[SYSTEM]: ERROR. INVALID ANSWER.')
  
  return inptUsr














'''
Documentation:
  - if x is a list, do a copy to avoid nested list
    x[:] create a shallow copy 

  - isinstance(value, type) checks the type of value

  - x: value  ||  _: accumulator  ||  n: number
    [x for _ in range(n)

  - long form of the function CreateCustomArr
    def createCustomArr(x: any, n:int):
      if (isinstance(x, list)): return x[:]
      else: return x for _ in range(n)
'''