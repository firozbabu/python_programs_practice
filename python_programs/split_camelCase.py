p = 'ILikeApples'
t = list()
s=p[0][-1]
position=0
for i in range(1,len(p)):
    if(s.isupper() and p[i].isupper()):
        
        t.append(''.join(s))
        print(s)
        s=p[i]
    else:
        s+=p[i]
        print(s)
print(t)
        
