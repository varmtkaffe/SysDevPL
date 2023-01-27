'''
Using keys and indexing, grab the 'hello' from the following dictionaries: d1 = {
'simple_key':'hello'} d2 = {'k1':{'k2':'hello'}} d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
'''

d1 = {'simple_key':'hello'} 
d2 = {'k1':{'k2':'hello'}} 
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#print(d1)  # {'simple_key': 'hello'}
#print(d1.keys()) # dict_keys(['simple_key'])

print(d1['simple_key'])

print(d2['k1']['k2'])

print(d3['k1'][0]['nest_key'][1][0])