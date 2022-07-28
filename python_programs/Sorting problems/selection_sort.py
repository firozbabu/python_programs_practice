#SELECTION SORT

nums = [45,100,0,1,-5,-10,4,5,6,13]

for i in range(len(nums)-1):
    index = i
    for j in range(i,len(nums)):
        #if nums[j] < nums[index]: #ascending order
        if nums[index] < nums[j]: #descending order
            index = j
    if index != i:
        nums[index],nums[i] = nums[i],nums[index]

print(nums)
