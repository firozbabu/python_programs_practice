def merge(arr):
    if len(arr)==1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right  = arr[mid:]

    merge(left)
    merge(right)

    i=0
    j=0
    k=0

    while i<len(left) and j<len(right):

        if left[i]>right[j]: #descending order #replace > with < for ascending order
            arr[k]=left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

arr=[5,1,9,0,4,1,7,9,1,3,41,2,9,6,4,6,1,0]
merge(arr)
print(arr)
