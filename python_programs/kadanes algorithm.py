
'''

#arr = [-2,1,-3,4,-1,2,1,-5,4]

#arr = [1]
arr = [5,4,-1,7,8]
for i in range(1,len(arr)):
    if arr[i-1] >0:
        arr[i] += arr[i-1]
print(max(arr))
'''



nums = [-3,1,-8,12,0,-3,5,-9,4]
current_sum = 0
max_sum = 0
for i in nums:
    current_sum += i
    if current_sum<0:
        current_sum = 0
    if max_sum < current_sum:
        max_sum = current_sum
print(max_sum)
