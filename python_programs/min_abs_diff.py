#minimum absolute difference between elements

'''
from math import inf
arr = [4,2,1,3]

min_diff = inf
result = []
for  i in range(len(arr)):
    for j in range(i+1,len(arr)):
        min_diff = min(min_diff,abs(arr[i]-arr[j]))


for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        t = [0]*2
        
        if min_diff == abs(arr[i]-arr[j]):
            print(arr[i],arr[j])
            if arr[i]<arr[j]:
                t[0]=arr[i]
                t[1] = arr[j]
                result.append(t)
            else:
                t[0]=arr[j]
                t[1] =arr[i]
                result.append(t)
            
result.sort()
print(result)
'''

from math import inf
arr = [4,2,1,3]
arr.sort()
result = []
min_diff = inf
for i in range(len(arr)-1):
    min_diff = min(min_diff,abs(arr[i]-arr[i+1]))

for  i in range(len(arr)-1):
    if min_diff==abs(arr[i]-arr[i+1]):
        result.append([arr[i],arr[i+1]])
print(result)

