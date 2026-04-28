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