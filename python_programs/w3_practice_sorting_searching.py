#w3resources sorting and searching

#problem-1


'''
def binary_search(list,ele):
    low = 0
    high = len(list)-1
    
    while low<=high:
        mid = (low+high)//2
        if list[mid] == ele:
            return True
        else:
            if list[mid]<ele:
                low  = mid+1
            else:
                high = mid-1
    return False

print(binary_search([1,2,3,5,8],6))
print(binary_search([1,2,3,5,8],5))
'''


#problem-2

'''
def sequential_search(list,ele):
    for i in range(len(list)):
        if list[i] == ele:
            return True,i
    return False

print(sequential_search([11,23,58,31,77,43,12,65,19],31))
'''



#problem-3

'''
def ordered_binary_search(list,ele):
    low = 0
    high = len(list)-1
    
    while low<=high:
        mid = (low+high)//2
        if list[mid] == ele:
            return True
        else:
            if list[mid]<ele:
                low  = mid+1
            else:
                high = mid-1
    return False

print(ordered_binary_search([0,1,3,8,14,18,19,34,52],3))
print(ordered_binary_search([0,1,3,8,14,18,19,34,52],17))
'''


#problem-4

'''

list = [14,46,43,27,57,41,35,21,70]
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j]<list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]

print(list)
'''
