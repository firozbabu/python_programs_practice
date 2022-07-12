#1

'''
n = int(input())
arr = list(map(int,input().split()))
count = 0
for i in arr:
    if not i:
        arr.remove(i)
        arr.append(i)
print(*arr,sep=' ')
'''


#2
'''
p = int(input())
p = list(bin(p)[2:])
for i in range(len(p)):
    if p[i] == '0':
        p[i] = '1'
    else:
        p[i] = '0'
print(int(''.join(p),2))
'''

#3

p  = list(map(int,input().split()))
for i in range(len(p)):
    for j in range(i,len(p)-1):
        if p[i] > p[j+1]:
            p[i],p[j+1] = p[j+1],p[i]
print(p)
