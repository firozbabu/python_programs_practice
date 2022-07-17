#wiggle sort


#nums = [3,5,2,1,6,4]
#nums = [0,5,3,2,2]
#nums = [-2,-5,-45] 
nums = [-2.1,-5.68,-45.11]




for  i in range(len(nums)):
    if (i%2==1)==(nums[i-1]>nums[i]):
        nums[i-1],nums[i] = nums[i],nums[i-1]


print(nums)


#google coding interview
nums = [-2.1,-5.68,-45.11]
for i in range(len(nums)):
    if (i%2==1 and nums[i] < nums[i-1]) or (i%2==0 and nums[i] > nums[i-1]):
        nums[i],nums[i-1] = nums[i-1],nums[i]

print(nums)
