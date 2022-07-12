def twoSum( nums,target):
        su=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    su.append(i)
                    su.append(j)
        return list(set(su))
nums=list(map(int,input().split()))
target=int(input())
print(twoSum(nums,target))


'''
or
'''


for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
