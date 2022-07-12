# cook your dish here
'''
a,b=input().split()
if int(a)%5==0 and int(a)<=float(b):
    b=float(b)-int(a)
    b-=0.50
    print('{:.2f}'.format(float(b)))
else:
    print('{:.2f}'.format(float(b)))
'''
'''
n=int(input())
for i in range(n):
    a=list(map(int,list(input())))
    print(a.count(4))
  '''
'''
n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    if 7 in a:
        print('YES')
    else:
        print('NO')
   '''


'''
n=int(input())
p=sorted(int(input()) for j in range(n))
for i in p:
    print(i)
'''
'''
n=int(input())
p=list(map(lambda x:x.strip('0'),[input() for i in range(n)]))
for i in p:
    print(int(i[::-1]))
'''
'''
n=int(input())
p=[sorted(set(map(int,input().split()))) for i in range(n)]
for i in p:
    print(i[-2])
'''
'''
n=int(input())
for i in range(n):
    t,a=list(map(int,input().split()))
    p=a
    for j in range(t):
        p+=sum([i for i in range(1,p)])
    print(p)
'''
'''
from math import prod
n=int(input())
p=[list(map(int,input().split())) for i in range(n)]
l=[prod(i)-prod(i)*0.1 if i[0]>1000 else prod(i) for i in p ]
print(l)   

'''
'''
from math import sqrt
n=int(input())
for i in range(n):
    m=int(input())
    print(round(sqrt(m)))
'''
'''
n=int(input())
for i in range(n):
    p,q=list(map(int,input().split()))
    print(p%q)
'''

'''
a = int(input())
t = ['normal','huge','small']
r = t[0]
for j in range(a):
    t.insert(len(t),t.pop(0))
    print(t)
    r = t[0]
print(r)
'''

'''
for i in range(int(input())):
    n = int(input())
    d = {}
    for j in range(n):
        p,a = list(map(int,input().split()))
        if 1<=p<=8 and p not in d:
            d[p]=a
        else:
            if not p>8:
                 d[p]=max(d[p],a)
    if d:
        print(sum(d.values()))
    else:
        print(0)
'''
'''
num = 10
p = [1,2,4,3,6]
'''

'''
for i  in range(len(p)):
    for j in range(i+1,len(p)):
        for k in range(j+1,len(p)):
            if p[i]+p[j]+p[k] ==num:
                print(p[i],p[j],p[k])
'''


'''
n = int(input())
m = list(map(int,input().split()))
p = 0
for j in m:
    if p > j:
        p -= abs(p-j)
    elif p<j:
        p += abs(p-j)
print(p)
'''

d = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',
     10:'ten',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundered'}


def f(t):
    r = str(t)
    if len(r)==2:
        print(d[int(r[0]+'0')])
        print(d[int(r[-1])])
f(39)
        

    
