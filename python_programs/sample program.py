#print('Meme programmers')
'''
str1=[i for i in str1]
str2=[i for i in str2]
s1copy = str1.copy()
s2copy = str2.copy()
for i in str1:
    if i in str2:
        s1copy.remove(i)
for j in str2:
    if  j in str1:
        s2copy.remove(j)
return ''.join(s1copy+s2copy)
'''



'''
arr = [[0 for y in range(total+1)]for x in range(k+1)]

for i in range(total+1):
  arr[0][i] = 0
  arr[1][i] = 1

for i in range(k+1):
  arr[i][0] = 0
for row in range(2,k+1):
  for col in range(1,total+1):

    if col < row:
      arr[row][col] = arr[row-1][col]
    elif col == row:
      arr[row][col] = arr[row-1][col] + 1
    else:
      arr[row][col] = arr[row-1][col]  +  arr[row][col-row]

return arr[k][total]
'''
'''
m,x,n,y,c=list(map(int,input().split(',')))
p=0
for i in range(n):
  for j in range(m):
    if (i*y+j*x)==c:
      p+=1
print('Possible' if p else 'NotPossible')
'''



'''
N=int(input())
A=list(map(int,input().split()))
t = 0
while len(A)>=3:
  r=0
  j=0
  for i in range(N):
    r1 = A[(i-1+N)%N]*A[i]*A[(i+1)%N]
    if r1>=r:
        if A[j]<A[i] and r==r1:
            pass
        else:
            j=i
            r=r1
  t+=r
  A.pop(j)
  N-=1
print(t)
'''





'''
from itertools import combinations as cb
c=0
for i in range(M):
    A[L[i]-1],A[R[i]-1]=A[R[i]-1],A[L[i]-1]
    for j in cb(A,2):
        if j[0]>j[1]:
            c+=1
return c%26                    
'''



'''
from itertools import combinations
a=int(input())
b=list(map(int,input().split()))
if(a<=1):
    print(0)
else:
    c=min(list(combinations(b,2)),key=lambda x:x[0]-x[1])
    print(c[1]-c[0])
'''
'''
n=int(input())
m=list(map(int,input().split()))
ans=1
for i in range(1,m+1):
    ans=(ans*i)%(10**9+7)
print(ans)

'''








'''








return ''.join(str(j) for j in sum(sorted([[i,input1.count(i)] for i in set(input1)],key=lambda x:x[0]),[]))

'''


'''

return int(max(itemID))
'''
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=input().split()
p=[list(map(int,input().split())) for i in range(int(a))]
d=list(map(lambda x:sum(i**2 for i in x)%int(b),p))
print(d)
'''
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a=list(map(int,input().split()))
v=list(map(int,input().split()))
print(*product(a,v))

'''
'''
from itertools import groupby
a=input()
p=[(len(list(j)),int(i)) for i,j in groupby(a)]
print(p)

'''
'''

cube = lambda x: x**3# complete the lambda function 
print(cube)
def fibonacci(n):
    # return a list of fibonacci numbers
    l=[0,1]
    if n<=1:
        return l[0]
    else:
        for i in range(2,n):
            l.append(l[i-2]+l[i-1])
            print(l)
        return l
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))



'''

'''

from itertools import combinations
n=input()
l=[]
count=1
for i in range(2,len(n)):
    for j in list(combinations(n,i)):
        if ''.join(j) !=''.join(j)[::-1]:
            count+=1
        print(j)
print(count)
    
'''


'''
n=int(input())
p=list(map(int,input().split()))
a=int(input())
t=[p[i:i+a] for i in range(0,len(p)-a+1)]
count=0
for i in t:
    if sum(i)%2==0:
        count+=1
if count:
        print(count)
else:
    print(-1)
'''
'''
num=list(map(int,input().split()))
count=0
for i in set(num):
    if(num.count(i)>1):
        count+=1
print(count)
'''

'''

a=[]
for i in range(5):
    n=int(input())
    if(n>=42 and int(str(n)[-1])==1):
        a.append(-6)
    elif(n>=42):
        a.append(-4)
    elif(int(str(n)[-1])==1 and n>=0):
        a.append(-5)
    elif(n>=0):
        a.append(n)
print(*a,sep='\n')
'''




'''
N,D=list(map(int,input().split()))
p=[]
count=0
for i in range(N):
    p.append(input().split())
if(N<=1):
    print(0)
else:
    for j in range(N-1):
        for k in range(j+1,N):
            if(p[j][:2]==p[k][:2][::-1]):
                if(0<int(p[k][2])-int(p[j][2])<=D):
                    count+=1
                    break
    print(count)
'''



'''
n=int(input())
word=[]
for i in range(n):
    count = 0
    a,b=input().split()
    if a=='add':
        word.append(b)
    else:
        for j in word:
            if j.startswith(b):
                count+=1
        print(count)
'''

'''
p=input1.split()
return ' '.join(reversed(p))
'''


'''
d=input3
dic={}
m=input2
for i in range(0,input1):
    if(d[i] not in dic.keys()):
        dic[d[i]]=m[i]
    else:
        dic[d[i]]=max(m[i],dic[d[i]])
return sum(dic.values())
'''


'''

for i in arr:
    if i==b:
        b+=b
return b


'''

'''
n=input()
print(eval('*'.join(n)))
'''



'''
n=input()
print(sum(list(map(lambda i:not i.isalnum() and not i.isspace(),n))))
'''



'''
a=int(input())
num=(1000,900,500,400,100,90,50,40,10,9,5,4,1)
rom=('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I')
for i in range(a):
    n=int(input())
    res=''
    for i in range(len(num)):
        count=int(n/num[i])
        res+=str(rom[i]*count)
        n-=num[i]*count
    print(res)
'''



'''
n=input()
r = [i for i in n if n.count(i)==1]
if len(r)>=2:
    print(r[1])
else:
    print('Invalid String')
'''
'''
n = input()
r = 0
for i in n:
    if n.count(i) == 1:
        r+=1
    if r==2:
        print(i)
        break
else:
    print('Invalid String')
'''


'''
t= int(input())
for i in range(t):
    res=0
    n=int(input())
    s=input()
    while True:
        if(s.find('01')!=-1):
           s = s.replace('01','')
        elif s.find('10')!=-1:
           s = s.replace('10','')
        else:
            break
        res+=1
    if res%2==0:
        print('Joe')
    else:
        print('John')
            
    '''

'''

from itertools import accumulate
p=[]
for i in range(5):
    p.append(int(input()))
m=list(accumulate(p))
print(*m,sep='\n')

'''




'''

s1 = set()
s2 = set()
for i in range(input1):
    s1.add(input2[i][0])
    s2.add(input2[i][1])
n = sum(input2,[])
f = sum((map(lambda i:n.count(i)>1,n)))
r = 8*(len(s1)+len(s2))+1-f
return r
'''
'''
arr = list(map(int,input().split()))
x=int(input())
p=[]
for i in arr:
    p.append(x+i)
    x=x+i
print(p)
'''















'''
import string
alphabet = string.ascii_lowercase
word = input().lower()
distances = {}
for l, c in zip(word, 'a' + word[:-1]):
    distances[l] = min(abs(alphabet.index(l) - alphabet.index(c)), 26 - abs(alphabet.index(l) - alphabet.index(c)))  
return sum(distances.values())
'''








m,n,p,*lists = list(map(int,input().split(',')))
res1 = sum(lists[:m])
res2 = sum(lists[m:])
count = 0
while True:
    if res1>0:
        res1-=5
        count+=1
    elif res2>0:
        res2-=10
        count+=1
    else:
        break
if count<=p:
    print("Yes")
else:
    print("No")










