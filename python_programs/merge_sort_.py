

def merge(arr):

    if len(arr)==1:
        return


    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge(left)
    merge(right)

    i=j=k=0


    while i<len(left) and j<len(right): 
    

        #if left[i]<right[j]:#ascending order
        if left[i]<right[j]: #descending order
             arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k] = right[j]
        j+=1
        k+=1

arr = [6,3,9,0,6,1,-4,-6,-1,-67,-4,-1,-23]
print(arr)
merge(arr)
print(arr)
