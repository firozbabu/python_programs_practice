n = input()
t = n[0]
c = 1
for i in range(1,len(n)):
    if t[-1]!=n[i]:
        t+=n[i]
        c+=1
    else:
        t+=str(c)
        c=1
print(t)
	
