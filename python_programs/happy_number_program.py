n = int(input())
count = 0
while True and len(str(n))!=1:
    count = sum(int(i) for i in str(n))
    n = count

    if n==1:
        print(True)
        break

print(count)
