# Create an array with x value of size n
# x: value  ||  _: accumulator  ||  n: number
# [x for _ in range(n)

def createCustomArr(x, n):
  # if x is a list, do a copy to avoid nested list
  # x[:] create a shallow copy 
  # isinstance(value, type) checks the type of value

  # simplify form
  return [x[:] if isinstance(x, list) else x for _ in range(n)]

  '''
  long form
  ---------------------------------------
  if (isinstance(x, list)): return x[:]
  else: return x for _ in range(n)
  '''

