#spy number 1124 ( 1*1*2*4 == 1+1+2+4)


#1st way
'''
n = input()
print(eval('+'.join(n)))
print(eval('*'.join(n)))
'''

#2nd way
'''
n = input()
s = 0
p = 1
for i in n:
    i = int(i)
    s+=i
    p*=i
print(s,p)
'''

#3rd way
'''
n = int(input())
sum=0
prod = 1
while n:
    t = n%10
    prod*=t
    sum+=t
    n = n//10

print(sum,prod)
'''


#find spy numbers with in the range

'''
for i in range(10000):
    t = str(i)
    sum = eval('+'.join(t))
    prod = eval('*'.join(t))
    if sum==prod:
        print(i)

'''


