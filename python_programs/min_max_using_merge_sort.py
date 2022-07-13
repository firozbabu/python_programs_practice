#this program is not working

def merge(arr,start,end):

    if start==end:
        max = arr[start]
        min = arr[start]

    elif start+1==end:
        if arr[start]<arr[end]:
            max = arr[end]
            min = arr[start]
        else:
            max = arr[start]
            min = arr[end]
    else:
        mid = (start+end)//2
        left = merge(arr,start,mid)
        right = merge(arr,mid,end)

        if left[0]>right[0]:
            max = left[0]
        else:
            max = right[0]
        if left[1]<right[1]:
            min = left[1]
        else:
            min = right[1]
    return min,max


arr = [4,2,0,8,20,9,2]
print(merge(arr,0,len(arr)-1))




'''

arr = [4,2,0,8,20,9,2]
n = len(arr)
if n%2!=0:
    max = arr[0]
    min = arr[0]
    i=1
else:
    if arr[0]<arr[1]:
        max = arr[1]
        min = arr[0]
    else:
        max = arr[0]
        min = arr[1]
    i=2

while i<n:
    if arr[i]<arr[i+1]:
        if arr[i]<min:
            min = arr[i]
        if arr[i+1]>max:
            max = arr[i+1]
    else:
        if arr[i]>max:
            max = arr[i]
        if arr[i+1]<min:
            min = arr[i+1]
    i=i+2

print(min,max)


'''






