def counting_for_radix(arr,place_value):
    countarray = [0]*10
    size = len(arr)
    for i in range(size):
        place_el = (arr[i]//place_value)%10
        countarray[place_el] +=1
    for i in range(1,10):
        countarray[i] += countarray[i-1]
    outputarray = [0]*size
    i = size-1
    while i>=0:
        current = arr[i]
        place_el = (arr[i]//place_value)%10
        countarray[place_el] -=1
        outputarray[countarray[place_el]] = current
        i-=1
    return outputarray


def radix_sort(arr):
    max_el  = max(arr)
    d = 1
    while max_el>0:
        max_el /=10
        d+=1
    place_value = 1
    outputarray = arr
    while d>0:
        outputarray = counting_for_radix(outputarray,place_value)
        place_value *=10
        d-=1
    return outputarray


arr = [2,20,61,997,1,619]
print(radix_sort(arr))
