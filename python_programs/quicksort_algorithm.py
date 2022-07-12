






arr = [8,9,0,6,5,3,1,4,5,-6,5,2,3,9,7,10]


def partition(arr,p,r):

    x = arr[r]

    i = p-1
    for j in range(p,r):
        if arr[j]<=x:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return i+1


def quicksort(arr,p,r):
    if p<r:
        q = partition(arr,p,r)
        quicksort(arr,p,q-1)
        quicksort(arr,q+1,r)



quicksort(arr,0,len(arr)-1)
print(arr)


