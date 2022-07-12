"""
to find the spy number

1124 => 1*1*2*4 == 1+1+2+4


"""


p = int(input())
sum = 0
prod = 1
while p:
    t = p%10
    sum+=t
    prod*=t
    p//=10


print(sum==prod)
