#find  whether any two numbers from list add upto k


#brute force approach


'''
list_of_numbers = [10,15,3,7]
k = int(input())
for i in range(len(list_of_numbers)):
    for j in range(i+1,len(list_of_numbers)):
        if list_of_numbers[i]+list_of_numbers[j] == k:
            print(list_of_numbers[i],list_of_numbers[j])
'''



#using two pass hash table

'''
target = 9
list_of_numbers = [2,7,11,15]
p = {}
for i in range(len(list_of_numbers)):
    p[list_of_numbers[i]] = i 


for i in range(len(list_of_numbers)):

    r = target - list_of_numbers[i]
    if (r in p) and (p[r] !=i):
        print([i,p[r]])
        break
    
'''
#using one pass hash table

target  = 9
nums = [2,7,11,15]
hashmap = {}
for i in range(len(nums)):
    comp  = target - nums[i]
    if ( comp in hashmap ):
        print([i,hashmap[comp]])
        break
    hashmap[nums[i]] = i


hashmap = {}
for i in range(len(nums)):
    complement = target - nums[i]
    if complement in hashmap:
        print([hashmap[complement],i])
    hashmap[nums[i]] = i



















