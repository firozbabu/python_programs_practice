p = [5, 3, 2, 4] 

i = 0
j = 2

min = 100

while i<len(p)-2:
    if min > abs(p[i]-p[j]):
        min = abs(p[i]-p[j])
        print(p[i],p[j])
        j+=1
    else:
        j+=1
    if j==len(p)-1:
        i+=1
        j=i+1

print(min)
