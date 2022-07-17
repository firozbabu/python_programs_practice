#test cases

#this program is for only sorted list
'''
assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({-6, -2, 4, 7, 12, 17}, -4) == -6
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5


'''


arr = [5]
low = 0
high = len(arr)-1
target = 5
while low <=high:
    mid = (low+high)//2
    if arr[mid]==target:
        print(arr[mid])
        break
    elif arr[mid]<target:
        low =mid+1
    elif arr[mid]>target:
        high = mid-1


        
if low ==0:
    print(arr[0])
elif low ==len(arr):
    print(arr[len(arr)-1])
else:
    if target-arr[low-1]<arr[low]-target:
        print(arr[low-1])
    elif target-arr[low-1]>arr[low]-target:
        print(arr[low])
    else:
        print(min(arr[low],arr[low-1]))
