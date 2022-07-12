#insertion sort

nums = [1,-5,10,100,-4,0,3,2,1]
for i in range(len(nums)):
    j = i
    while j>0 and nums[j-1] > nums[j]:
        nums[j-1], nums[j] = nums[j], nums[j-1]
        j-=1
print(nums)
