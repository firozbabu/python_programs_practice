arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
from random import randrange

for i in range(len(arr)-1,-1,-1):

    j = randrange(i+1)
    arr[j],arr[i] = arr[i],arr[j]

print(arr)
    
