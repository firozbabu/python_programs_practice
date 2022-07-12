from collections import Counter
o=list(map(str,input().split()))
p=[]
for i in range(0,len(o)):
    k=[]
    for j in range(i,len(o)):
        if(Counter(o[i])==Counter(o[j])) and :
            k.append(o[j])
    else:
        p.append(k)
print(p)
