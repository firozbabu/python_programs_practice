def merge(t):
    if len(t)==1:
        return
    mid = len(t)//2
    left = t[:mid]
    right = t[mid:]
    merge(left)
    merge(right)
    i=0
    j=0
    k=0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            t[k]=left[i]
            i+=1
        else:
            t[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        t[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        t[k]=right[j]
        j+=1
        k+=1
t = [0,100,12,13,1,98,99,-4,-6,-5,-100]
merge(t)
print(t)
        
