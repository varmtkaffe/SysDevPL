# Problem 1: 
'''
Instructions: 
Given the string: 
s = 'Lexicon'
Use indexing to print the out the following:
'L'
'n'
'Lexi'
'con'
'on'
Bonus: Use indexing to reverse the string
'''

s = 'Lexicon'

'''
print(s[:1]) # L
print(s[6:]) # n
print(s[:4]) # Lexi
print(s[4:]) #con
print(s[5:7]) #on
'''

'''
my_list = list(s.split(' '))
print(my_list)
'''
'''
x = [i for i in s]
print(x[0])
#print(x) #['L', 'e', 'x', 'i', 'c', 'o', 'n']
'''

'''
my_list = list(s)
print(my_list) # ['L', 'e', 'x', 'i', 'c', 'o', 'n']

print(my_list[::len(my_list)]) #['L']

x = list(map(list,my_list))
print(x) # [['L'], ['e'], ['x'], ['i'], ['c'], ['o'], ['n']]
'''
''' 
x =  ''.join(my_list) # joins all items on the list without spaces. '' means no spaces.
'''

my_list = list(s)
#print(my_list)

print(my_list[0])
print(my_list[6])
print(''.join(my_list[:4]))
print(''.join(my_list[4:]))
print(''.join(my_list[5:7]))


my_list.reverse()
print(''.join(my_list))