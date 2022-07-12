'''
def prime(givenNumber,i=2):
    if i>givenNumber//2:
        print(givenNumber)
        return
    if givenNumber%i==0:
        return
    i+=1
    return prime(givenNumber,i)
prime(20)
'''

'''
def f(a,b=[]):
    return eval(str(b)[0]+f'{a}'.translate(str.maketrans('','','[]{}()'))+str(b)[1])
print(f([[[([1,2,3]),{1,2,}]]],[]))
'''

'''
with open('coding.py','r') as a:
    with open('copy_file.txt','w') as t:
        for i in a:
            t.write(i)
'''


'''
p = [1,2,2,2,3,4,4,5,5,5,1,1,1,5,4,3,2,4,2,4,6,6,6,8,1,2,5,4,8]
t = [p[0]]
l = []
for i in range(1,len(p)):
    if p[i] in t:
        t.append(p[i])
    else:
        l.append((t[0],t))
        t=[]
        t.append(p[i])
print('using normal method')
print(l)

print('using group by method')
from itertools import groupby
N=[]
for k,j in groupby(p):
    N.append((k,list(j)))
print(N)
'''


'''
sequence = [1, 3, 2]
i=0
A=False
while i==0:
    ele = sequence.pop(i)
    sq=sequence.copy()
    if sorted(set(sequence))==sq:
        A=True
        i+=1
    else:
        A=False
    
if A:
    print('true')
else:
    print('false')
'''


'''
for i in range(int(input())):
    a,b= list(map(int,input().split()))
    p = list(map(int,input().split()))
    t = ''
    for j in p:
        if b>=j:
            b-=j
            t+='1'
        else:
            t+='0'
    print(t)
'''
'''
for i in range(int(input())):
    A,B,A1,B1,A2,B2  = list(map(int,input().split()))
    if {A,B}=={A1,B1}:
        print(1)
    elif {A,B}=={A2,B2}:
        print(2)
    else:
        print(0)
'''

'''
for i in range(int(input())):
    d_DSA,d_TOC,d_DM = list(map(int,input().split()))
    s_DSA,s_TOC,s_DM = list(map(int,input().split()))
    if sum([d_DSA,d_TOC,d_DM]) > sum([s_DSA,s_TOC,s_DM]):
        print('DRAGON')
    elif sum([d_DSA,d_TOC,d_DM]) == sum([s_DSA,s_TOC,s_DM]):
        if d_DSA > s_DSA:
            print('DRAGON')
        elif d_DSA == s_DSA:
            if d_TOC > s_TOC:
                print('DRAGON')
            elif d_TOC == s_TOC:
                if (d_DM > s_DM):
                    print('DRAGON')
                elif d_DM == s_DM:
                    print('TIE')
            else:
                print('SLOTH')
        else:
            print('SLOTH')
    else:
        print('SLOTH')

'''
'''
def f(a):
    d =[]
    k = a[0]
    print('first',k)
    for i in range(1,len(a)):
        if a[i] != k[-1]:
            d.append((k[0],k.count(k[0])))
            k=a[i]
            print('second',k)
            
        else:
            k+=a[i]
            print('third',k)
    d.append((k[0],k.count(k[0])))
    return ['count of {0} is {1}'.format(i,j) for i,j in d]
print(*f(['*','*','*','@','*','*','*',]),sep='\n')
'''


 
'''
from itertools import groupby
def f(a):
    p = [(i,len(list(j))) for i,j in groupby(a)]
    return ['count of {0} is {1}'.format(i,j) for i,j in p]
print(*f(['*','*','*','@','*','*','*','#','#']),sep='\n')
'''
'''
for i in range(int(input())):
        a,b,c,d = list(map(int,input().split()))
        print(max(a-c,b-d))
'''


'''
from math import ceil
for i in range(int(input())):
        c,b= list(map(int,input().split()))
        e,o = c//2,ceil(c/2)
        e1,o1=b//2,ceil(b/2)
        print(e*e1+o*o1)
'''

'''
for i in range(int(input())):
   for j in range(int(input())):
       a,b,c=list(map(int,input().split()))
       team_a=0
       team_b=0
       if a==1:
           print('YES')
           team_a+=b
           team_b+=c
       else:
           if team_a==0 or team_b==0:
                   print('NO')
           else:
                   if (team_a > b):
                           print('YES')
                           team_a+=c
                           team_b+=b
                   elif (team_a <b and team_a>c):
  '''




'''
a = int(input())
bike=0
car=0
while a>2:
   car+=1
   a-=4
if a!=0:
   a-=2
   bike+=1
if (car>0 and bike>0) or bike>0:
    print('YES')
else:
    print('NO')
'''
'''
for i in range(int(input())):
   b,a = list(map(int,input().split()))
   banana=0
   while b!=0 and a!=0:
      b-=2
      banana+=1
      a-=1
   print(banana)
'''
'''
   if b>a:
       print(b//2)
   elif b<a:
       print(a)
'''
'''
from collections import Counter
s=input()
p = Counter(s)
m = max(p.values())
n = min(p.values())
if list(p.values()).count(m)==1 and m-n==1:
   print('YES')
else:
   print('NO')
'''
'''
a  = list(map(int,input().split()))
bob=0
andy=0
while a:
   r = max(a)
   bob+=1
   a=a[:a.index(r)]
   try:
      r=max(a)
      a=a[:a.index(r)]
      andy+=1
   except:
      pass
if bob>andy:
   print('BOB')
else:
   print('ANDY')
'''
'''
s= {1:'one', 2: 'two', 3: 'three', 4: 'four', 
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine',10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
        14: 'fourteen', 15: 'quarter', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen',20: 'twenty', 21: 'twentyone', 22: 'twentytwo', 22: 'twentytwo', 23: 'twentythree', 
        24: 'twentyfour', 25: 'twentyfive', 26: 'twentysix', 27: 'twentyseven',28: 'twentyeight', 29: 'twentynine',30:'half'}
h = int(input())
m = int(input())



  
   
def f(h,m,p):
   
       if m==0:
          return f'{s[h]} o` clock'
       elif m==15:
          return f'{s[m]} {p} {s[h]}'
       elif m==1:
          return f'{s[m]} minute {p} {s[h]}'
       elif m>1:
          return f'{s[m]} minutes {p} {s[h]}'
       elif m==30:
          return f'{s[m]} {p} {s[h]}'
if m>30:
       print(f(h+1,60-m,'to'))
else:
       print(f(h,m,'past'))

'''

'''
from itertools import combinations
items = int(input())
k = int(input())
l = [int(input()) for i in range(items)]
l.sort()
a = []
for i in range(0,len(l)+1,k):
   if len(l[i:i+k])==k:
      print(l[i:i+k])
      a.append(max(l[i:i+k])-min(l[i:i+k]))
print(min(a))
'''

''' WwRONG
for i in range(int(input())):
   p = int(input())
   a = [list(map(int,input().split())) for i in range(p)]
   for i in range(len(a)):
      for j in range(len(a[0])-1):
         if a[i][j]==0:
            if sum(a[i])==sum(a[i+1]):
               print('posible')
            else:
               print('Impossible')
         else:
            if (a[i][j] -:=1 == a[i+1][j]+=1) and (sum(a[i])==sum(a[j+1-i])):
               print('Impossible')
'''
'''
p = 'GFGF'
i = 0
u =[]
d = {}
while i!=len(p):
   for j in range(i,len(p)+1):
      if p[i:j]:
         u.append(p[i:j])
   i+=1
print(u)
for i in u:
   if i not in d:
      d[i]=1
   else:
      d[i]+=1
print(d)
'''

'''
p = int(input())
a = list(map(int,input().split()))
i  = sorted([(i,j)  for i ,j in enumerate(a,1)],key= lambda i:i[1],reverse = True)
print(*[k for k , j in i])
'''

'''
n, ma = list(map(int,input().split()))
group  = list(map(int,input().split()))
t = []
i = 1
while i!=n+1:
    for j in range(0,n,i):
        t.append(group[j:j+i])
        print
    i+=1
t= list(filter(None,t))
t = list(filter(lambda i:sum(i)<=ma,t))
print(t)
print(len(t))
'''




'''
from collections import Counter
from math import floor
a = 'baab'
r = str(a[0])
for i in range(1,len(a)):
    if a[i]!=r[-1]:
        r+=a[i]
print(r)
'''
'''
from itertools import groupby
import copy
a = 'baab'
t = ''
s=True
while s:
    print(a)
    for i,j in groupby(a):
        if len(list(j))%2!=0:
            t+=list(j)[0]
            
    a=copy.deepcopy(t)
    t=''
    if set(a)!=list(a):
        s = False
print(a)
if a:
    print(a)
else:
    print('EMpty string')
'''

'''
x = [0,1,1]
y = [0,1,2]
n = int(input())
for i in range(3,n+1):
    x+=[y[i-1]]
    y+=[x[i-1]+y[i-1]]
result = x[n]+y[n]
print(result*result)
'''


'''
n = int(input())
t = int(input())
a = list(map(int,input().split()))
a.sort()
count = 0

for i in a:
    if t-i>0:
        t-=i
        count+=1
    if t<=1:
        break
print(count)

'''




'''
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = 0
for i in range(n):
    c1 = 0
    for j,k in zip(a,b):
        if j==k:
            c1+=1
    if c1>c:
        c=c1
    a.append(a.pop(0))
print(c)

'''



'''
p = [wordCountFirstLine,wordCountSecondLine]
if wordCountSecondLine<wordCountFirstLine:
    return 'Invalid input'
else:
    for i in range(totalLines):
        p.append(p[-1]+p[-2])
    return p[totalLines-1]
    
'''
'''
n = int(input())
p = list(map(int,input().split()))
negative = 0
positive = 0
zero = 0
for i in p:
    if i==0:
        zero+=1
    elif i<0:
        negative+=1
    else:
        positive+=1
print(*['{:.6f}'.format(i/len(p)) for i in [positive,negative,zero]],sep='\n')
'''
'''
p = int(input())
k = [int(input()) for i in range(p)]
w = []
for i in k:
    t = i
    while True:
        if t%5==0:
            break
        t+=1
    if (t-i)<3 and not (t<40):
        w.append(t)
    else:
        w.append(i)
    
print(w)
'''
'''
candles = list(map(int,input().split()))
print(candles.count(max(candles)))
 '''
'''
arr  = list(map(int,input().split()))
d = {}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(max(d,key = lambda k:d.get(k)))
'''
'''
p = [list(map(int,input().split())) for i in range(int(input()))]
i = 0
s = 0
w = 0
for j in range(len(p)):
    s+=p[i][j]
    i+=1
for k in range(len(p)):
    w+=p[i-1][k]
    i-=1
print(abs(s-w))
'''
'''
p = list(map(int,input().split()))
d,m = list(map(int,input().split()))
i = 0

count = 0
while i<len(p):
    if sum(p[i:i+m]) == d:
        count+=1
    i+=1

print(count)
'''
'''
n = int(input())
p = int(input())
t = []
i = 0
for j in range(2,p+1,2):
    i+=1
t.append(i)
i = 0
for j in range(n-1,p):
    i+=1
t.append(i)
print(t)
print(min(t))
print(n-p)
'''






'''
n = int(input())
s = input()
s_l = list(s)
c = list(map(int,input().split()))
ans = 0
sc = list(zip(s,c))


def f(q,c1):
    d = list(zip(q,c1))
    min_cost = 0
    n = len(q)
    count = 0
    for i in range(0,n//2,2):
        if q[i]!=q[n-i-1]:
                a = [d[i],d[n-i-1]]
                q[n-i-1] = max(a,key = lambda i:i[1])[0]
                print('maximum',max(a,key = lambda i:i[1])[0])
                count+=1
                print('q',q[n-i-1])
                print('1',q)
                print('count',count)
                print('ans',ans)
                if q[i+1]!=q[n-i-2]:
                    a = [d[i+1],d[n-i-2]]
                    q[n-i-2] = max(a,key = lambda i:i[1])[0]
                    count+=1
                    print('2',q)
        elif q[i]!=q[n-i-2]:
                a = [d[i],d[n-i-2]]
                q[n-i-2] = max(a,key = lambda i:i[1])[0]
                min_cost+=1
                if q[i+1]==q[n-i-1]:
                    a = [d[i+1],d[n-i-1]]
                    q[n-i-1] = max(a,key = lambda i:i[1])[0]
                    min_cost+=1
    return count if count<=min_cost else min_cost



for i in range(0,n//2,2):
    if (s[i] == s[n-i-1] and s[i+1]==s[n-i-2]) or (s[i] == s[n-i-2] and s[i+1]==s[n-i-1]) :
        continue
    else:
        
        if s[i]==s[n-i-1]:
            if not (s[i+1]==s[n-i-2]):
                a = [sc[i+1],sc[n-i-2]]
                s_l[n-i-2] = max(a,key = lambda i:i[1])[0]
                ans +=1
        elif s[i]!=s[n-i-1]:
                ans+=f(s_l[i:n-i],c[i:n-i])
                print('s_l',s_l[i:n-i])
print(ans)

'''

'''
n = set(map(int,input().split()))
for i in range(int(input())):
    l1 = set(map(int,input().split()))
    l2 = set(map(int,input().split()))
    print(n.issuperset(l1) and n.issuperset(l2))
'''

'''
from itertools import product
a,b = list(map(int,input().split()))
p = [list(map(int,input().split()))[1:] for i in range(a)]

m = 0
for i in sorted(p):
    m+=max(i)**2
print(m%b)

m = 0
for i in product(*p):
    s = sum(i)%b
    if s>m:
        m = s
print(m)
'''
'''
n = int(input())
p = input().split()
a = int(input())

from itertools import combinations

t = list(combinations(range(1,len(p)+1),a))
s = []
for i in range(len(p)):
    if p[i]=='a':
        s.append(i+1)
print(t)
print(s)

list(filter(lambda x,y:
'''

'''
a = input().replace(' ','')
p = [input() for k in range(int(input()))]
p = ''.join(p)
if len(p)>len(a):
    print('NO')
else:
    count = 0
    for k in p:
        if k in a:
            count+=1
    if count==len(p):
        print('YES')
    else:
        print('NO')
'''

'''
string = 'abc'
count = []
p = string[0]
for i in range(1,len(string)):
    if p[-1]==string[i]:
        p+=string[i]
        
    else:
        count.append(len(p))
        p=string[i]
    count.append(len(p))



if any(i for i in count if i>1):
    print(True)
else:
    print(False)
'''


'''
def conver(list_number):
    return list(map(str,list_number))

list_number = list(map(int,input().split()))
print(convert(list_number))
'''

'''
    
for i in range(int(input())):
    N,M = list(map(int,input().split()))
    a=list(map(int,input().split()))
    p = [abs(M-i) for i in range(N)]
    q=[]
    for j in a:
        q.append([abs(j-k) for k in range(N)])
    if len(q)>1:
        print(*[max(i) for i in zip(*q)])
    else:
        print(*p)

'''
'''
p = 'test 5 a0A pass007 ?xy1' .split()
l = []
for i in p:
    if i.isalnum():
        digit = 0
        letters = 0
        for j in i:
            if j.isdigit():
                digit += 1
            elif j.isalpha():
                letters+=1
        if digit%2!=0 and letters%2==0:
            l.append(len(i))
if l:
    print(max(l))
else:
    print(-1)
'''


'''
if len(a)==1:
    print(1)
else:
    
    for i in range(len(a)):
        if a[j]==-1:
            p.append(j)
            p.insert(len(p),a[j])
            break
        else:
            p.append(j)
            j = a[j]
    print(p,j)
'''
'''

for i in range(len(a)):
        if a[j]==-1:
            p.append(j)
            p.insert(len(p),a[j])
            break
        else:
            p.append(j)
            j = a[j]
print(p,j)
'''

'''
a = [1,2,4,5,7,29,30]
p = list(range(1,31))
for i in p:
    t = list(range(1,i+1))
    if len(t) == 7:
        print(t)
  '''




'''
p = list(intialStr)
n = int(input())
for i in range(n):
    a,b,c  = input().split()
    p[int(a):int(b)+1]=c
    t.append(list(p))
m = 0
for j in range(n-1):
    for k in range(j+1,n):
        if t[j] == t[k] and m<k-j:
            m = k-j
print(m)
  '''
'''
import itertools  
n = int(input())
p = []
for i in range(2,n+1):
    t = bin(i)[2:]
    if 1<=len(t)<=len(str(n)) and t[0]!='0':
        p.append(t)
'''
'''
s = set()
s_s_f  = 0
for i in p:
    s_s_f+=int(i)
    if (s_s_f - n) in s:
        print(True)
        break
    s.add(s_s_f)
print(s)
'''

'''
for i in range(1,len(p)+1):
    for j in itertools.combinations(p,i):
        if sum(map(int,j)) == n:
            print(j)

'''
'''
mod = 1000000007
d = {}

def solve(X,i,j):
    sum1 = 0
    if i==0  or j==0:
        return X%mod
    for p in range(i+1):
        if (p,j-1) in d:
            pass
        else:
            d[(p,j-1)] = solve(X,p,j-1)
        sum1+=d[(p,j-1)]
    return sum1

print(solve(17,14,25))
'''
'''
import decimal
decimal.getcontext().prec = 100000
x = 17
i = 14
j = 25
'''



s = 468
a = [135,101,170,125,79,159,163,65,106,146,
     82,28,162,92,196,143,28,37,192,5,103,154,
     93,183,22,117,119,96,48,127,172,139,70,113,
     68,100,36,95,104,12,123,134]

'''
for i in range(len(a)+1):
    for j in range(i+1,len(a)+1):
        if sum(a[i:j]) == s:
            print(i+1,j)
            print(a[i:j])
'''


'''
i = 0
j = 1
while i<=j:
    print(i,j)
    if i==j:
        break
    else:
        if j == len(a):
            i+=1
            j = i+1
        else:
            if sum(a[i:j])==s :
                print(a[i:j])
                break
        j+=1
'''




s = 'Dl )B 4(V! A. MK, YtG ](f 1m )CNxuNUR {PG?'

temp = '.,-?abcedeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for x in s.split():
    for y in x:
        if y in temp:
            continue
        else:
            s.remove(x)
            break
print(s)
print(len(s))
