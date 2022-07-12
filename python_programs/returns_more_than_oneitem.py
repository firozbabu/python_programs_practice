t = [1,2,3,4,2,2,3,1,4,4,4,5,5,6,7,6,5]

d = {}
s = set()

for i in t:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for i in d:
    if d[i]>1:
        s.add(i)

print(min(s))
print(d)
print(s)
