arr  = [0,1,2,2,1,0,0,2,0,1,1,0]
start = mid = 0
end = len(arr)-1
pivot = 1

while mid<=end:

    if arr[mid]<pivot:
        arr[start],arr[mid] = arr[mid],arr[start]
        start +=1
        mid +=1
        print(arr)
        print('start',start)
        print('mid',mid)
        print('end',end)
    elif arr[mid]>pivot:
        arr[mid],arr[end] = arr[end],arr[mid]
        end -=1
        print(arr)
        print('start',start)
        print('mid',mid)
        print('end',end)
    else:
        mid +=1

print(arr)


'''  
max_el = max(arr)
c = [0]*(max_el+1)
for i in arr:
    c[i] +=1

for i in range(1,len(c)):
    c[i]+=c[i-1]

o = [0]*(len(arr))
i=len(arr)-1
while i>=0:
    current = arr[i]
    c[current]-=1
    o[c[current]] = current
    i-=1

print(o)
'''
