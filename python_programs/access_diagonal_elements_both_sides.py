n = int(input())
p = []
for i in range(n):
    p.append(list(map(int,input().split())))

k = 0
l  = len(p)
first = []
second = []
for j in range(len(p)):
    first.append(p[j][k])
    second.append(p[j][l-1])
    k+=1
    l-=1

print(*first)
print(*second)

        
