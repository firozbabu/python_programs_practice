arr = [3,5,1,2,0,8,5,4,3,90,76,223,6565,-7,233,8]
print(arr)

'''
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] < arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
'''

has_swapped = True
while has_swapped:
    has_swapped = False
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            has_swapped=True
        
print(arr)
