#dutch national flag alogrithm

arr  = [1,0,2,2,0,1,1]
#arr = [2,0,1,1,0]
low = 0
high  = len(arr)-1
mid = 0
while mid<=high:

    if arr[mid]==0:

        arr[mid],arr[low] = arr[low],arr[mid]
        low+=1
        mid+=1
    elif arr[mid]==1:
        mid+=1
    else:
        arr[mid],arr[high] = arr[high],arr[mid]
        high -=1
print(arr)
