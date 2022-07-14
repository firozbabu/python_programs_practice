#problem - 1
# calculate sum of list of numbers


'''
def s(l):
    if len(l)==0:
        return 0
    return l[0]+s(l[1:])

print(s([1,2,3,4,5,6,7,8,9,10]))
print(s([2,4,5,6,7]))
'''


#problem-2
#calculate factorial of non-negative number

'''
def fact(n):
    if n<1:
        return 1
    return n*fact(n-1)

print(fact(10))
print(fact(5))
'''


#problem-3
#get factorial of non-negative number

'''
def st(n):
    if n==0:
        return 0
    return n%10+st(n//10)

print(st(345))
print(st(45))
'''

#problem-4
#sum of positive integers until n+(n-2)+n(n-4)...n-x=<0
'''
def f(n):
    if n < 1:
         return 0
    return n+f(n-2)

print(f(6))
print(f(30))
'''


#problems-5
#calculate harmonic sum until n-1





