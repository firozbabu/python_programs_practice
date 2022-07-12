#question-1


'''
l = []
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        l.append(i)
print(l)
'''


#question-2


'''
n  = int(input())
p=1
for i in range(1,n+1):
    p *= i
print(p)
'''
'''
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(8))
'''

#question-3


'''
n = int(input())
d = {i:i*i for i in range(1,n+1)}
print(d)
'''

#question-4


'''
p = input().split(',')
print(p)
print(tuple(p))
'''

#question-5

'''
class A:
    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())

st = A()
st.getString()
st.printString()
'''


#question-6
'''
from math import sqrt
c = int(input())
d = int(input())
h = int(input())
print(sqrt((2*c*d)/h))
'''



