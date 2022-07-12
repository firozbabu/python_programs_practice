t = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

#print(max(t,key=t.get))

#print(list(t))


'''
keys = ['a', 'b', 'c', 'd', 'e', 'f']
values = [1, 2, 3, 4, 5]
p = dict(zip(keys,values))
print(p)
'''

#print([i for i,j in t.items() if j==20])


#r = {'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
'''
d = {}
for i in r.values():
    if type(i)==dict:
        y = list(i.values())
        d[y[0]]=y[1]

print(d)
'''


students = [
  { 'name': 'Theodore', 'age': 18 },
  { 'name': 'Mathew', 'age': 22 },
  { 'name': 'Roxanne', 'age': 20 },
  { 'name': 'David', 'age': 18 }
]
'''
p = [x.get('age') for x in students]
print(p)
'''
'''

t = {10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}
p = {value:key for key,value in t.items()}
print(p)
'''




from functools import reduce 
from operator import getitem
def test(d, selectors):
  return reduce(getitem,selectors,d) 
users = {
  'Carla ': {
    'name': {
      'first': 'Carla ',
      'last': 'Russell' 
    },
    'postIds': [1, 2, 3, 4, 5]
  }
}




'''


Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.


from functools import reduce 
from operator import getitem
def test(d, selectors):
  return reduce(getitem, selectors, d) 
users = {
  'Carla ': {
    'name': {
      'first': 'Carla ',
      'last': 'Russell' 
    },
    'postIds': [1, 2, 3, 4, 5]
  }
}
print(test(users, ['Carla ', 'name', 'last']))
print(test(users, ['Carla ', 'postIds', 1]))
'''



