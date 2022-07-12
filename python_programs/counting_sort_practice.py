
arr = [2,2,3,52,65,7,2,0,6,43,6,5]
max_element = max(arr)
c = [0]*(max_element+1)


for i in arr:
    c[i]+=1


for i in range(1,len(c)):
    c[i]+=c[i-1]


o = [0]*len(arr)
i = len(arr)-1

while i>=0:
    current = arr[i]
    c[current]-=1
    o[c[current]] = current
    i-=1
print(o)
