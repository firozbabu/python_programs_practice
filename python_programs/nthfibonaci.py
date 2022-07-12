
'''
import os
import sys
from math import sqrt
import decimal
n = 1000
decimal.getcontext().prec = 10000
root5 = decimal.Decimal(5).sqrt()
phi = (1+root5)/2
a = round(((phi**n)-((-phi)**-n))/root5)
print(sys.getsizeof(a))
'''




p = [0,1]
while True:
    
    p.append(p[-1]+p[-2])
    if len(str(p[-1])) == 3:
        print(p.index(p[-1]))
        print(p[-1])
        break
    

    
'''
def f(n):
    if n<2:
        return n
    return f(n-1)+f(n-2)
print(f(40))
'''

'''
import decimal
from math import sqrt
n = 4
decimal.getcontext().prec = 10000
root5 = decimal.Decimal(5).sqrt()
phi = (1+root5)/2
r = ((phi**n)-((-phi)**(-n)))/root5
print(round(r))
'''
