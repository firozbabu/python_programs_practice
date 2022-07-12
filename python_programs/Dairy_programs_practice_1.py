"""
to find the spy number

1124 => 1*1*2*4 == 1+1+2+4


"""

'''
p = int(input())
sum = 0
prod = 1
while p:
    t = p%10
    sum+=t
    prod*=t
    p//=10


print(sum==prod)

'''


l  = [[1,2,3,4],[4,3,2,1],[7,8,9,6],[6,5,4,3]]

k  = 0
m = len(l)


left_diag = []
right_diag=[]
for i in range(len(l)):
    left_diag.append(l[i][k])
    k+=1
    right_diag.append(l[i][m-1])
    m-=1

print(left_diag)
print(right_diag)
