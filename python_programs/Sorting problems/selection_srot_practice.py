arr = [5,3,0,2,4,1,6,3,5,1,9,6,7,1,3,94]
print(arr)

for i in range(len(arr)):
    j = i
    for k in range(i,len(arr)):
        if arr[k]<arr[j]:
            j=k
    if j!=i:
        arr[j],arr[i] = arr[i],arr[j]
print(arr)
