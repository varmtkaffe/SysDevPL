"""
Given a string, return a string where for every char in the original, there are two chars.
doubleChar('The') → 'TThhee' doubleChar('AAbb') → 'AAAAbbbb' doubleChar('Hi-There') → 'HHii--TThheerree'

"""
""" def doubleChar(str):
 for i in str:
  x = i+i
  print(x, end="") """


def doubleChar(str):
  for i in str:
    for j in i:
      print(j+i, end='')
      
  print('')
    

doubleChar('The')
doubleChar('AAbb')
doubleChar('Hi-There') 