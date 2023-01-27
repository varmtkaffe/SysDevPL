"""
Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.
For example:
arrayCheck([1, 1, 2, 3, 1]) → True arrayCheck([1, 1, 2, 4, 1]) → False arrayCheck([1, 1, 2, 1, 2, 3]) → True

"""

"""
def find_seq(arr):
 for i in range(len(arr)):
  if (arr[i], arr[i + 1], arr[i + 2] == (1,2,3)):
   return True
  else:
   return False

  
arr1 = [1, 1, 2, 3, 1]
arr2 = [1, 1, 2, 4, 1]
arr3 = [1, 1, 2, 1, 2, 3]

print(find_seq(arr1))
print(find_seq(arr2))
print(find_seq(arr3))
"""

arr1 = [1, 1, 2, 3, 1]
arr2 = [1, 1, 2, 4, 1]
arr3 = [1, 1, 2, 1, 2, 3]

def myFunc(n):
 for i in range(len(n)):
  #print(i)
  #print(n)
  x = list(set(n))
  #print(x)
  if x[i] == 1 and x[i + 1] == 2 and x[i + 2] == 3:
   return True
  else:
   return False

print(myFunc(arr1))
print(myFunc(arr2))
print(myFunc(arr3))

#This is the solution without else if statements
'''
def check_seq(arr):
 return any((arr[i], arr[i + 1], arr[i + 2]) == (1,2,3) for i in range(len(arr) - 2))

print(check_seq(arr))
'''
