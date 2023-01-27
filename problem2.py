# Given this nested list:
my_list = [3,7,[1,4,'hello']]
#Reassign "hello to be "goodbye"

'''
print(my_list) # prints [3, 7, [1, 4, 'hello']]

3 index 0 on the list
7 index 1 on the list
[1,4,'hello'] index 2 on the list

Then the items within the list of index 2 have their own index.
1 index 0
4 index 1
'hello' index 2

print(my_list[2][2]) # This prints hello
'''
'''
print(my_list)
print(my_list[2][2])
my_list = my_list[2].append('goodbye')

'''

my_list[2].insert(2,'goodbye')
x = my_list[2].pop(3)
print(my_list)