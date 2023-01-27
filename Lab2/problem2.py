"""
Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo".
For example:
stringBits('Hello') → 'Hlo' stringBits('Hi') → 'H' stringBits('Heeololeo') → 'Hello'

"""

def stringBits(str):
 for i in str:
  return str[::2]
 """ for i in range(0, len(str), 2):
  print(str[i]) """
  #print("This is i: ", i)
  #for x in str[i]:
   #print("This is x: ", x)
   #print(str[i], end="")

str1 = 'Hello'
str2 = 'Hi'
str3 = 'Heeololeo'

print(stringBits(str1))
print(stringBits(str2))
print(stringBits(str3)) 


"""
print(i)
x = str[i]
print(x)
if (i % 2) == 0:
 print(x)
"""
 

