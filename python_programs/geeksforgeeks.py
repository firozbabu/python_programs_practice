'''
from string import ascii_lowercase
n = int(input())
a= ascii_lowercase
b = a[::-1]
str1 = input().lower()
str1 = list(str1)
for i in range(n-1,len(str1)):
    str1[i] = b[a.index(str1[i])]

print(''.join(str1))
'''

'''
string = input().split()
print(''.join(string))
'''


str1 = input()
c1 = input()
c2 = input()
str1 = list(str1)
'''
for i in range(len(str1)):
    if str1[i] == c1:
        str1[i] = c2
    elif str1[i] == c2:
        str1[i] = c1
print(''.join(str1))
'''

k = map(lambda x: x if (x!=c1 and  x!=c2) else c1 if x == c2 else c2,str1)
print(''.join(k))

