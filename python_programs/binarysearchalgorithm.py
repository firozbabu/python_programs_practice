
'''
low = 0
high = len(a)-1
k  = 1
def f(a,k,low,high):
    while low<=high:
        mid = (low+high)//2
        if k==a[mid]:
            return a[mid],k
        elif k>a[mid]:
            low = mid +1
        else:
            high = mid-1
print(f(a,k,low,high))
'''


'''
def binarysearch(a,k,low,high):
    if low>high:
        return False
    else:
        mid = (low+high)//2
        if k==a[mid]:
            return mid,a[mid],k
        elif k>a[mid]:
            return binarysearch(a,k,mid+1,high)
        else:
            return binarysearch(a,k,low,mid-1)
print(binarysearch(a,6,0,len(a)-1))
'''



a  = [1,2,5,6,8,12,34]
def binary(a,k,low,high):
    while low<=high:
        mid = (low + high)//2
        if k == a[mid]:
            return f'element {a[mid]}  found at index {mid}'
        elif k>a[mid]:
            low = mid+1
        else:
            high = mid-1
    return 'element not found'

print(binary(a,5,0,len(a)-1))
 



'''
a  = [1,2,5,6,8,12,34]
def recursive ( a,k,low,high):
    print('low',low,'high',high)
    if low>=high:
        return 'element not found'
    else:
        mid  = (low+high)//2
        if k == a[mid]:
            return f' element {a[mid]} found at index {mid}'
        elif k>a[mid]:
            return recursive(a,k,mid+1,high)
        else:
            return recursive(a,k,low,mid-1)

print(recursive(a,0,0,len(a)-1))
'''








