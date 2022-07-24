arr = [1,2,3,4,5,6,7,8,9,10]
i = len(arr)//2
j = len(arr)-1

while i>0:
    temp = arr[i]
    i-=1
    arr[i]=arr[j]
    j-=1
    arr[j] = temp

print(arr)
    
