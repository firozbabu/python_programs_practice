def partition(s,e):

    p = s+(e-s)//2
    nums[e],nums[p] = nums[p],nums[e]
    new_p = s
    for i in range(s,e):
        if nums[i] <nums[e]:
            nums[new_p],nums[i] = nums[i],nums[new_p]
            new_p +=1
    nums[e],nums[new_p] = nums[new_p],nums[e]
    return new_p

def quickselect(nums,k):

    l = 0
    h = len(nums)-1
    while l<=h:

        p  = partition(l,h)
        if p<k:

            l = p+1
        elif p>k:
            h = p-1
        else:
            return nums[p]
    return nums[p]

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(quickselect(nums,len(nums)-k))


nums = [3,2,3,1,2,4,5,5,6]
nums.sort()
print(nums[len(nums)-k])
