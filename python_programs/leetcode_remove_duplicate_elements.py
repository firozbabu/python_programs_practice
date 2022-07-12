nums=list(map(int,input().split()))
rem=[]
for i in nums:
    if i not in rem:
        rem.append(i)
count=len(nums)-len(rem)
for i in range(count):
    rem.append('_')
print(rem)
