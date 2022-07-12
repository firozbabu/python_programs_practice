
'''

a,b= list(map(int,input().split(' ')))
c=list(map(int,input().split(' ')))
if(b in c):
    print(c.index(b))
else:
    for i in c:
        if(i >b):
            print(c.index(i))
            break
            

'''


'''
a,r,n = list(map(int,input().split(' ')))
print(a*(r**(n-1)))


'''


'''
a= int(input())
a=str(a)
b=0
for i in a:
    if(int(i)%2==0):
        b+=int(i)
print(b)

'''



'''
a=int(input())
b=list(map(int,input().split(' ')))
print(len(list(filter(lambda x : x>=0,b))))
a=input()
s=sum(int(i)**len(a) for i in a)
print(s)
'''




'''

a=input()
b='abcdefghij'
res=''
for i in a:
    res+=b[int(i)]
print(res)
'''




'''
a=input()
b=[]
for i in range(0,len(a),2):
    b.append(max(a[i:i+2]))
print(''.join(b))
'''


'''
def findthirdlastconsonant(b):
    a=('a','e','i','o','u')
    count=3
    for i in reversed(b):
        if i not in a:
            count-=1
            if count==0:
                return i
a=int(input())
b=input()
print(findthirdlastconsonant(b)


'''
'''
import heapq
a=int(input())
b=list(map(int,input().split(' ')))
result = heapq.nlargest(2,b)
print(sum(result))

import string
a= int(input())
b=input()
letters = string.ascii_lowercase
for i in b:
'''
'''
def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        elif(char.isdigit()):
            result+=chr((ord(char) + s-47)%10 +48)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

s=int(input())
text=input()
print (encrypt(text,s))

'''
'''
time=6
friends=3
from itertools import repeat
print(sum(list(repeat(  ,time)),[])[time-2:time+1])
'''



'''
    
a=raw_input()
print int(min(a))
    
'''



'''
result=''
if (str1==str2 or str1 == '' or str2==''):
    return None
else:
    for i in str1:
        if(i  not in str2):
            result+=i
        else:
            str2=str2.replace(i,'')
    return result+str2
'''
'''
weights=list(map(int,input().split()))
sum_weights = sum(weights)

if sum_weights%2==0:
    print(sum_weights//2)

'''
'''
n = int(input('Enter number of weights'))
lst = []
for i in range (0,n):
weights = int(input('weight %s ='%i))
lst.append(weights)
sum_weights=sum(lst)
if sum_weights%2==0:
print(sum_weights//2)
'''
'''
a=int(input())
b=input()
u=l=''
for i in b:
    if(i.isupper()):
        u+=i
    else:
        l+=i
u = sorted(u)
l = sorted(l)
r=''
j=k=0
for i in range(a):
    if ord(b[i])<97:
        r+=u[j]
        j+=1
    else:
        r+=l[k]
        k+=1
print(r)

a  = list(filter(lambda x:x.isupper(),'dfadGH'))
c  = list(filter(lambda x:x.islower(),'dfadGH'))
'''



'''
    def anagram(str1,str2):  
        list1 = list(str1)  
        list2 = list(str2)  
        list1.sort()  
        list2.sort()  
        return (list1 == list2)
    result=[]
    for  i in sentences:
        count = 0
        for j in i.split():
            for k in wordSet:
                if(anagram(j,k)) and j!=k:
                    count+=1
        result.append(2*count)
    return result

   '''









'''
from itertools import permutations
a = list(map(int,input().split()))
b = list(permutations(a))
b.pop(0)
count=0
for i in b:
    if i[0]<i[1] and i[1]<i[2]:
        count+=1
print(count)

lst = list(map(int,input().split()))
sum_weights=sum(lst)
def w():
    for i in range(len()):
        for j in r
'''

'''
from itertools import permutations
a=int(input())
b=int(input())
d=list(range(a,b))
c=permutations(d,2)
result=0
if a>b:
    print(-1)
elif (a==b):
    print(0)
else:
    for i in c:
        if i[0]^i[1]>result :
            result=i[0]^i[1]
    print(result)


a=input()
r=0
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        if a[i:j] == ''.join(reversed(a[i:j])):
            r+=1
            print(a[i:j])
print(r)

x=int(input())
n=int(input())
m=int(input())
n1=n**x-1
m1=m**x-1
if(n>=m):
    print(m1+n1)
else:
    print(m1-n1)

'''

'''
from math import sqrt
a = int(input())
b = list(map(int,input().split()))
count=0
for i in b:
    c = int(sqrt(i))
    if c**2==i:
        count+=1
print(count)
'''





'''
if(len(arr)==1):
    return int(arr[0])
else:
    return eval('^'.join(map(str,arr)))
'''
'''
a= list(map(int,input().split()))
b=list(map(int,input().split()))
result=a[::]
for i in b:
    if i not  in a:
        result.append(i)
print(result)
'''
'''
nums=list(map(int,input().split()))
re=sorted(nums)
for i in range(len(re)+1):
    if((i not in re ) and (re[i-1] < i)):
        print(i)
'''


'''
res=int(''.join(map(str,num1)))-int(''.join(map(str,num2)))
a=[]
for i in str(res):
    a.append(int(i))
return a
'''


'''
    e = [0]
    a, d= zip(*sorted(zip(arrival, duration)))

    for i in range(len(arrival)-1):
        if a[e[-1]]+d[e[-1]] <= a[i+1]:
            e.append(i+1)
        elif a[e[-1]]+d[e[-1]] >= a[i+1]+d[i+1]:
            e.pop()
            e.append(i+1)

    return len(e)

    '''



'''
    m = len(after)
    n = len(after[0])
    for i in range(m-1,-1,-1):
        for j in range(n-1,0,-1):
            after[i][j] -=after[i][j-1]
    
    for i in range(m-1,0,-1):
        for j in range(n-1,-1,-1):
            after[i][j] -=after[i-1][j] 
    
    return after

'''

'''
n= len(s)
dp = [[0 for a in range(n)] for b in range(n)]
for i in range(n):
    dp[i][i] = 1
    for r in range(n-2, -1, -1):
        for c in range(r+1, n):
                if s[r] == s[c]:
                    dp[r][c] = 2 + dp[r+1][c-1] 
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c-1])
print(dp[0][-1]*dp[0][-2])
'''
'''
s='acdapmpomp'
N = len(s)
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
    for r in range(N-2, -1, -1):
        for c in range(r+1, N):
            if s[r] == s[c]:
                dp[r][c] = 2 + dp[r+1][c-1] 
            else:
                dp[r][c] = max(dp[r+1][c], dp[r][c-1])
print(dp[0][-1]*dp[N-1][N-1])
print(dp)
'''
'''
import itertools
s='attract'
a=list(itertools.chain.from_iterable(itertools.combinations(s, i+1) for i in range(len(s))))
d=sorted({''.join(i) for i in a if ''.join(i)[::-1]==''.join(i)},key = lambda x: len(x))     
print(d)
print(res)
'''


'''
import itertools
s='attract'
a=list(itertools.chain.from_iterable(itertools.combinations(s, i+1) for i in range(len(s))))
d=sorted({''.join(i) for i in a if ''.join(i)[::-1]==''.join(i)},key = lambda x: len(x))
print(d)
print(res)
'''
'''
import itertools

s='attract'
l=[]
for r in range(len(s)+1):
    c=itertools.combinations(s,r)
    c_l=list(c)
    l+=c_l
print(l)

'''

'''
n=input()
a=[i for i in n if(n.count(i)==1)]
print(len(a))
'''

'''
a,b=input().split()
s=0
for i in range(int(a),int(b)+1):
    s+=eval('+'.join(str(i)))
print(s)
'''
'''
from itertools import combinations
a=int(input())
b=list(combinations(map(int,input().split()),2))
c=int(input())
count = 0
for i in b:
    if sum(i) == c:
        count+=1
print(count)

'''








'''

a=input()
b=input()
q=0
for i,j in zip(a,b):
    q+=ord(j)-ord(i)
print(q)
'''






'''
import string
q=string.ascii_letters+string.digits+'+-_@.'
if(len(address)<258):
    def E164(s):
        if((s[0].isdigit() and len(s)<=15 and s[0]!=0) or ( not s[0].isdigit() and len(s)<=16 and s[1]!=0) ) and s[1:].isdigit():
            return True
        else:
            return False
    b=''
    c=''
    if ':' in address:
        b,c=address.split(':',1)
    if E164(address):
        return 'SMS')
    elif(b.upper()=='WHATSAPP'):
        if(E164(c)):
            return "WHATSAPP")
        else:
            return 'INVALID_ADDRESS')
    elif(b.upper()=="MESSENGER"):
        if(E164(c)):
            print('MESSENGER')
        else:
            print('INVALID_ADDRESS')
    elif(b.upper()=='WECHAT'):
        e=list(filter(lambda x: x in q,c))
        if(len(e)==len(c)):
            print("WECHAT")
        else:
            print('INVALID_ADDRESS')
    else:
        print('INVALID_ADDRESS')
else:
    print('INVALID_ADDRESS')
'''


'''
a=input()
count=0
for i in range(0,len(a)):
    if sorted(a[i:i+3]) == ['A','B','C']:
        count+=1
print(count)
    
'''



'''
def area(A):
    ans = 0
    A = [-1] + A
    A.append(-1)
    n = len(A)
    stack = [0]  
    for i in range(n):
        while A[i] < A[stack[-1]]:
            h = A[stack.pop()]
            area = h*(i-stack[-1]-1)
            ans = max(ans, area)
        stack.append(i)
    return ans
n=int(input())
A=list(map(int,input().split()))
print(area(A))
'''
'''

def sumSwap(nums1, nums2,n,m):
    count=0
    sum1 = sum(nums1)
    sum2 = sum(nums2)
    print(sum1)
    print(sum2)
    for i in range(n):
        for j in range(m):
            if (sum1 + nums1[j] - nums2[i]) == (sum2 + nums1[i] - nums2[j]):
                count+=1
    return count
print(sumSwap([1,4,20,2],[5,9,6,3],4,4))

'''
'''
n=0
m=0
A1 = []
A2=[]
r = []
for i in zip(A1,A2):
    r+=list(i)
if n>m:
    r+=A1[m:]
else:
    r+=A2[n:]
print(r)

'''

'''
    

from itertools import combinations
s = [2,4,6,9,10,12,15,16,18,19,22,27,29,31,32]
s = list(combinations(s,3))
for i in s:
    if sum(i)==n:
        print('{}+{}+{}={}'.format(i[0],i[1],i[2],sum(i)))


'''



'''
c=0
for j in range(len(a)):
    if j%2==0 and a[j]==a[0]:
        c+=1
if len(a)%2==0:
    if len(a)//2==c:
        return 1
    else:
        return 0
else:
    if len(a)//2+1==c:
        return 1
    else:
        return 0

'''


'''

from itertools import accumulate
n=int(input())
b=list(map(int,input().split()))
print(*list(accumulate(b)))

'''

'''
from math import ceil
a = int(input())
b = list(map(int,input().split()))
count=0
r = sum(b)
if round(r**(1/3))**3 == r:
    print('YES')
else:
    print(ceil(r**(1/3))**3 - r)

'''


'''
from string import ascii_lowercase
a = input()
b = ascii_lowercase[:9]
for i in a:
    print(b[int(i)],end='')
'''


'''
a = input()
b = []
for i in a:
    b.append(ord(i))
print(max(b)+min(b))
'''



'''
parts.sort()
r=[]
while len(parts)>1:
    r.append(sum(parts[:2]))
    parts.append(sum(parts[:2]))
    parts.pop(0)
    parts.pop(0)
    parts.sort()
return sum(r)
'''




'''
a=input()
if int(a)<1000000:
    if int(a[-1])<=5:
        a = a[:-1]+'0'
    else:
        a = a[:-2]+str(int(a[-2])+1)+'0'
    print(a)
else:
    print('Wrong Input')
   '''

'''
a = input()
r = 'N'
for i in a:
    if i=='L':
        if r[-1]=='N':
            r+='W'
        elif r[-1]=='W':
            r+='S'
        elif r[-1] == 'S':
            r+='E'
        else:
            r+='N'
    else:
        if r[-1]=='N':
            r+='E'
        elif r[-1]=='W':
            r+='N'
        elif r[-1] == 'S':
            r+='W'
        else:
            r+='S'

print(r[-1])    
'''
'''
import itertools
a=int(input())
b=int(input())
t=int(input())




 
iterable = list(range(0,b))
iter_obj = itertools.cycle(iterable)
for i in range(19):
     print(iter_obj[i])
'''


'''
n=int(input())
if(n%100!=0):
    print(int(n/100)+1)
else:
    print(int(n/100))
'''
'''
dueAmount = float(input())
totalAmount = float(input())
change = totalAmount - dueAmount
doller = change//1
i = round(change-doller,2)
quarter=0
while i>=0.25:
    i = round(i - 0.25,2)
    quarter+=1
dime = 0
print(i)
while i>=0.1:
    i=round(i-0.1,2)
    dime+=1
nickel = 0
print(i)
while i>=0.05:
    i=round(i-0.05,2)
    nickel+=1
pennis = 0
print(i)
while i>=0.01:
    i=round(i-0.01,2)
    pennis+=1
print(i)
print('{} Dollar\n{} Quater\n{} Dime\n{} Nickel\n{} Pennies'.format(doller,quarter,dime,nickel,pennis))
'''

'''
from collections import Counter
a=input()
n=int(input())
if(n>=1) and (n<=100):
    e=[]
    a=Counter(a)
    for i in a.items():
        if(i[1]==n):
            e.append(i[0])
    if(e):      
        e.sort()
        print(e[0])
    else:
        print('Wrong Input')
else:
    print('Wrong Input')
'''


'''
n=float(input())
t=float(input())
c=t-n
d=int(c//1)
qc=c-d
q=int(qc//0.25)
dc=round(qc-q*0.25,2)
di=int(dc//0.1)
dic=round(dc-di*0.1,2)
ni=int(dic//0.05)
nic=round(dic-ni*0.05,2)
p=int(nic//0.01)
print('{} Dollar\n{} Quater\n{} Dime\n{} Nickel\n{} Pennies'.format(d,q,di,ni,p))
'''
'''

from itertools import product
n=int(input())
a=list(product('AB',repeat=n))
c=0
for i in a:
    if 'AA' not in ''.join(i):
        c+=1
print(c)
'''








'''
a,*b=list(map(int,input().split(',')))
count=0
while True:
    for i in range(len(b)):
        count+=b[i]
        if count<1:
            count=i+1
            break
    else:
        break
if count-sum(b)==0:
    print(1)
else:
    print(count-sum(b))
  '''

'''

from math import ceil
n=int(input())
b=[input().split(',') for i in range(n)]
r=0
for i in b:
    r+=b[1]
    if b[1]>=2 and b[1]<=5:
        w = b[1]+b[1]/100
    elif b[1]>5 and b[1]<=10:
        w = b[1]+b[1]/500
    elif b[1]>10:
        w = b[1]+b[1]/1000
    if b[0]=='A':
         r+=w*10
    elif b[0]=='B':
         r+=w*25
    elif b[0]=='C':
         r+=w*20
    elif b[0]=='D':
         r+=w*125
    else:
        r+=w*1000
         
print(ceil(r))
print(b)

'''


'''
import string
a = string.ascii_uppercase
n=raw_input().lstrip('0')
k=True
if n== '':
    print -1
    k=False
elif int(n)<=25:
    print a[int(n)-1]
    k=False
n = map(int,n)
while k:
    r=sum(n)
    if r<26:
        print a[r-1]
        break
    else:
        n=map(int,str(r))

'''
'''
def f():
    n=int(input())
    input2=list(map(int,input().split()))
    e=[i for i in input2 if input2.count(i)>=2]
    return -1 if len(e)==0 else sorted(set(e))
print(f())
'''
'''
n=int(input())
m=int(input())
s=input()
t=input()
p=0
for i in range(n):
    t=t[-1]+t[1:-1]
    print(t)
    if t in s:
        p+=s.rindex(t)+1+s.index(t)
print(p)

'''



'''
S = list(S)
c=0
for i in range(len(S)):
    S.insert(0,S.pop())
    r = ''.join(S)
    for j in range(len(S)-len(query)+1):
        c += r.find(query,j,len(query)+j)+1
return c
'''


'''
K=int(input())
arr=[6272,9116,2429,9542]
c=arr[0]
p=[]
for i in range(1,len(arr)+1):
        p.append(c&arr[i])
        c=arr[i]
print(c)
print(p)
'''

'''
a=int(input())
b=list(map(lambda x : x.upper(),input().split()))
print(b)
count=[]
for i in b:
    for j in range(len(i)):
        print(i[j:len(i)-j],j)
        if(i[j:len(i)-j]==i[j:len(i)-j][::-1]):
            count.append(j-1)
            break

print(count)
'''
'''

def p(str):
    n = len(str)
    maxLength = 1
    start = 0
    for i in range(n):
        for j in range(i, n):
            flag = 1
            for k in range(0, ((j - i) // 2) + 1):
                if (str[i + k] != str[j - k]):
                    flag = 0
            if (flag != 0 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1
    return maxLength
b=list(map(lambda x : x.upper(),input().split()))
for i in b:
    print(p(i))
 '''





'''
return sum(range(i,j))+sum(range(j,k-1,-1)))
'''






if (input1 == 1): return 0
if (input1 == 2): return 1
return (input1 - 1) * (arrangements(input1 - 1) +arrangements(input1 - 2))




















