'''
def sum_n(n):
    if n<=0:
        return n
    else:
        return n+sum_n(n-1)
print(sum_n(10))
        
print(sum(range(11)))
'''

'''
def f(li):
    if li:
        return li[0]+f(li[1:])
    else:
        return 0
print(f([1,2,3,4,5,6,7,9,0,1]))


print(sum([1,2,3,4,5,6,7,9,0,1]))
'''

'''
def f(p):
    sum = 0
    for i in p:
        if isinstance(i,list):
            sum += f(i)
        else:
            sum+=i
    return sum

print(f([1,2,[3,4,[5,6,[7,8,[8,9]]]]]))


print(sum(eval('['+'[1,2,[3,4,[5,6,[7,8,[8,9]]]]]'.replace('[','').replace(']','')+']')))
'''


'''
def f(n):
    if n<=0:
        return 1
    else:
        return n*f(n-1)
print(f(30))
'''
'''
count = 1
for i in range(1,31):
    count*=i
print(count)
'''

'''
def f(n):
    if n<=0:
        return 0
    return n+f(n-2)
print(f(6))
'''


def f(n,a=1,b=1):
    
    c = a+b
    if n<2:
        return 0
    return c+f(n-1,b,c)
print(f(5))







