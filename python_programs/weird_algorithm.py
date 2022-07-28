

n = int(input())
l  = []
while n!=1:
    l.append(n)
    if n%2==0:
        n//=2
    else:
        n=(n*3)+1
l.append(1)
print(*l)
