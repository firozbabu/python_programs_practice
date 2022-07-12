''''

print('statement 1')
print('statement 2')
print('statement 3')
print('statement 4')
print('statement 5')
print('statement 6')

def block1():
    print('statement 1')
    print('statement 2')
    print('statement 3')
    print('statement 4')
    print('statement 5')
    print('statement 6')

def block2():
    print('statement 1')
    print('statement 2')
    print('statement 3')
    print('statement 4')
    print('statement 5')
    print('statement 6')

    def block3():
        print('statement 1')
        print('statement 2')
        print('statement 3')
        print('statement 4')
        print('statement 5')
        print('statement 6')


print('statement 10')


def block4():
    print('something')
'''










'''
def fun(a,b,c):
	b=c+a
	for c in range(2,6):
		a=11+c
		a=(b+c)^a
		a=9&c
	a=(9+1)^b
	return a+b
print(fun(5,6,6))
'''
'''
p,q,r=0,8,7
if(p>r):
        r=1+q
else:
        p=r+q
        if((r+q+p)>(p+r)):
                r=11+p
        r=7^q
        r=p+p
print(p+q+r)
'''


'''
from itertools import combinations
s="bb"
a=[]
for i in range(0,len(s)):
        a+=list(combinations(s,i))
        print(a)
print(max([''.join(i) for i in a if ''.join(i)[::-1]==''.join(i)],key=len) if len(s)!=1 else s[0])
'''
'''
import os
p=os.get_terminal_size()
print(p.columns)
'''




'''

from collections import defaultdict
a = defaultdict(list)
for i in arr:
    a[i[1]].append(i[0])
r = []
for i in sorted(a):
    r.extend(sorted(a[i]))
print(*r)
'''



'''

input2.sort()
res = 0
for i in range(input1-1):
    res+=abs(input2[i]-input2[i+1])
return res
'''




'''

r=''
for i in input1:
    if i not in r:
        r+=i
return r


'''

'''
import collections
a = 'ujnkdnnd'
b = collections.defaultdict(list)
for i in set(a):
    b[a.count(i)].append(i)
r = []
for i in sorted(b,reverse=True):
    r+=sorted(b[i],reverse=True)
print(r)


'''
'''
from itertools import combinations
def m(p):
    k = list(combinations(p,2))
    u = list(map(lambda i,j : (i*j)-(i+j),k))
    return max(u)
n = int(input())
p = list(map(int,input().split()))
print(m(p))


'''















'''




if True:
    print('true')
print('hello')
else:
    print('false')



'''





a = complex(input('Enter the complex: '))
print(type(a))


























































