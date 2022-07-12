def f(t):
    for j in range(2,t):
        if t%j==0:
            return False
    return True


n = int(input())
i = 2
while n!=1:
    if f(i):
        if i*n//i==n and i*f(n//i):
            print(n)
            n = n//i
            print(i)
        else:
            i+=1
    else:
        i+=1

