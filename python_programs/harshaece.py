




alphabets = input().split(',')
words = [input() for i in range(int(input()))]
new = alphabets.copy()
for i in words:
    for j in i:
        if j in new:
            new.remove(j)
    if len(alphabets)-len(i) == len(new):
        print('YES')
    else:
        print('NO')
        new = alphabets.copy()
