'''
from itertools import combinations
a=list(map(int,input().split()))
u=[]
for i in combinations(a,3):
    if  sum(i)==0 and sorted(i) not in u:
        u.append(sorted(i))   
print(u)

'''


'''
from itertools import combinations
l=list(map(int,input().split()))
p=l[:len(l)//2]
q=l[len(l)//2:]
print(max(p,q))

import math
print(dir(math))
'''


#single element in a sorted array

#input = [1,1,2,3,3,4,4,8,8]
#output = 2
# 2 is the element which count is 1



'''
nums = [1,1,2,3,3,4,4,8,8]
for i in range(len(nums)):
    if nums.count(nums[i])==1:
        print(nums[i])
'''

numbers = [5,25,75]
target = 100
i=0
j=i+1
while i!=len(numbers):
    while j!=len(numbers):
        print(numbers[i],numbers[j])
        if numbers[i] + numbers[j] == target:
            print([i+1,j+1])
        j+=1
    i+=1
    j=i+1
    print(i)
        




