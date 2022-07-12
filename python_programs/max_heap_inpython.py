def max_heap(a,k):
#https://favtutor.com/blogs/heap-in-python
    l = 2*k+1
    r = 2*k+2

    if l<len(a) and a[l]>a[k]:
        largest = l

    else:
        largest = k

    if r<len(a) and a[r]>a[largest]:
        largest = r

    if largest!=k:
        a[k],a[largest] = a[largest],a[k]
        max_heap(a,largest)


a = [3,9,2,1,4,5]
n = len(a)//2-1
for k in range(n,-1,-1):
    max_heap(a,k)
    
print(a)
