#problem -1

#given number is even or odd

'''
n = int(input())
print('odd' if n&1 else 'Even')
'''

#problem-2

#given number is prime or not


'''
n = int(input())
for i in range(2,n//2):
    if n%i==0:
        print('not a prime number')
        break
else:
    print('Prime Number')
'''

#problem-3
#given number is palindrome or not
'''
n= int(input())
rem =n
num=0
if n<0:
    print('Not a palindrome')
else:
    while n>0:
        print(num)
        num = (num*10)+(n%10)
        print(num)
        n=n//10
    print(rem==num)
'''



#problem-4
#to check given number is armstrong number
'''
for i in range(100000):
    n = i
    num = n
    d = 0
    while n>0:
        n//=10
        d+=1
    n=num
    sam = 0
    while num>0:
        sam+=(num%10)**d
        num//=10
    if n==sam:
        print(n,sam)
'''
#problem-5
#find factorial of number
'''
def fact(num):
    if num<=1:
        return 1
    else:
        return num*fact(num-1)
print(fact(5))

n=5
f = 1
for i in range(1,n+1):
    f*=i
print(f)
'''

#problem-6
#perfect number or not
'''
for j in range(10000):
    n = j
    sum = 0
    for i in range(1,(n//2)+1):
        if n%i==0:
            sum+=i
    if sum==n:
        print(sum,n)

'''


#problem-7
#strong number or not

'''

def fact(num):
    s=1
    for i in range(1,num+1):
        s*=i
    return s
for i in range(1,100000):
    n = i
    sam = n
    t=0
    while n>0:
        t +=fact(n%10)
        n//=10
    if t==sam:
        print(t,sam)
'''

#problem-8
#count no of digits in number
'''
n = int(input())
d=0
while n>0:
    n//=10
    d+=1
print(d)
'''

#problem-9
#program to swap two numbers (all methods)
'''
a = 4
b = 5

print(a,b)
#first method

a,b = b,a
print(a,b)


a = 4
b = 5
#second method
a = a+b
b=a-b
a=a-b
print(a,b)

a = 4
b = 5

#third method
a=a^b
b=a^b
a = a^b

print(a,b)
'''


#problem-10
#print fibonaci series
'''
n = int(input())

p = [0,1]
if n<=0:
    print(0)
if n==1:
    print(1)
if n==2:
    print(p)
else:
    for i in range(2,n):
        p.append(p[-1]+p[-2])
    print(p)

first =0
second = 1
for i in range(n):
    print(first)
    third = first+second
    first = second
    second = third
'''
#problem-11
#print odd and even numbers separately


'''
n = list(map(int,input().split()))
even = []
odd = []
for i in n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even,odd)


'''
#problem-12
#frequency of elements in array
'''
n = list(map(int,input().split()))
d = {}
for i in n:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''


#problem-13
#kadanes algorithm largest sum of contiguos array

'''
arr = [3,4,6,1,5,-6,-3,-1,7,2,9,0,1,4,3,2,8,9]
curr_sum = 0
max_sum = 0
start_index  = 0
end_index = 0
j=0
for i in range(len(arr)):
    curr_sum+=arr[i]
    if curr_sum<0:
        curr_sum=0
        j = i+1
    elif curr_sum>max_sum:
        max_sum = curr_sum
        start_index = j
        end_index = i
print(max_sum)
print(arr[start_index:end_index+1])
'''

#problem-14
#sort an array descending order using bubble sort
'''
arr = [3,4,6,1,5,-6,-3,-1,7,2,9,0,1,4,3,2,8,9]
for i in range(len(arr)):
    for  j in range(len(arr)-1):
        if arr[j+1]<arr[j]:
            arr[j+1],arr[j]=arr[j],arr[j+1]
print(arr)
'''

#problem-15
#search for an element in array using linear search
'''
arr = [3,4,6,1,5,-6,-3,-1,7,2,9,0,1,4,3,2,8,9]
for i in arr:
    if i==99:
        print('element found')
        break
else:
    print('element not found')
'''
#problem -16
#remove duplicates in array
'''
arr = [3,4,6,1,5,-6,-3,-1,7,2,9,0,1,4,3,2,8,9]
t = []
for i in arr:
    if i not  in t:
        t.append(i)
print(t)
'''

#problem-17
#find minimum and maximum in array

'''
arr = [3,4,6,1,5,-6,-3,-1,7,2,9,0,1,4,3,2,8,9]
min = arr[0]
max = arr[0]
for i in arr:
    if min>i:
        min =  i
    elif max<i:
        max = i
print(max,min)
'''

#problem-18
#find second largest number in array  | kth largest number
'''
arr = [3,4,6,1,5,-6,-3,-1,7,2,9,0,1,4,3,2,8,9]
k = 2


arr.sort()
print(arr)
print(arr[len(arr)-k])

#kth largest element means duplicate element also not kth distinct element
#arr = [3,2,3,1,2,4,5,5,6]
arr.sort(reverse=True)
print(arr)
print(arr[k-1])
'''
#problem-19
#conver binary to decimal

'''
number = 1001101
decimal = 0
i=0
while number!=0:
    last = number %10
    number//=10
    decimal = decimal+last*(2**i)
    i+=1
print(decimal)
'''

#binary to octal
'''
number = 1001101
octal =0
decimal = 0
i=0
while number!=0:
    decimal = decimal+(number%10)*(2**i)
    i+=1
    number //= 10
i=1
while decimal!=0:
    octal = octal+(decimal%8)*i
    decimal = decimal //8
    i=i*10
print(octal)
'''

#problem-20
#decimal to binary
'''
number = 77
binary = 0
i=1
while number !=0:
    rem = number%2
    number = number//2
    binary = binary+rem*i
    i=i*10
print(binary)
'''

#problem-21
#gcd of two numbers without recursion
'''
a = int(input())
b = int(input())
while b:
    a,b = b,a%b
print(a)
'''

#gcd for multiple values
'''
def find_gcd(a,b):
    while b:
        a,b = b,a%b
    return a

l = [2,4,6,8,16]
num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1,num2)
for i in range(2,len(l)):
    gcd = find_gcd(gcd,l[i])
print(gcd)
'''

#problem -22
#lcm of two numbers without recursion


'''
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

l = [2,4,6,8,16]
num1 = l[0]
num2 = l[1]

l_c_m = lcm(num1,num2) 
for i in range(2,len(l)):
    l_c_m = lcm(l_c_m,l[i])
print(l_c_m)

'''
#problem - 23
#find year is leap year or not

'''
year = int(input())

def leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)

print(leap(year))
'''

#problem-24
#find the volume of the sphere where radius is the input
#formula is 4/3 pi r**3
'''
from math import pi
r = int(input())
v = (4/3)*pi*r**3
print(v)
'''

#problem-25
#find area of the triangle with sides given
#formula h*b/2
#Area of Triangle with Three Sides (Heron’s Formula)
#sqrt(s(s-a)(s-b)(s-c))

from math import sqrt
a = int(input())
b = int(input())
c = int(input())
s = (a+b+c)/2

print(sqrt(s*(s-a)*(s-b)*(s-c)))
