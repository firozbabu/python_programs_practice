def radix_counting(arr,placevalue):

    countarray = [0]*10
    inputsize = len(arr)

    for i in range(inputsize):
        place = (arr[i]//placevalue)%10
        countarray[place]+=1

    #for j in range(1,10):
        #countarray[j] += countarray[j-1] #ascending order
    for i in range(10-2,-1,-1):  #descending order
        countarray[i]+=countarray[i+1]
        
    outputarray = [0]*inputsize
    i = inputsize-1

    while i>=0:
        current = arr[i]
        placeele = (arr[i]//placevalue)%10
        countarray[placeele]-=1
        newposition = countarray[placeele]
        outputarray[newposition]= current
        i-=1
    return outputarray







def radix(arr):

    m = max(arr)
    d = 1
    while m:
        m //=10
        d+=1

    placevalue = 1
    while d>0:
        arr = radix_counting(arr,placevalue)
        placevalue*=10
        d-=1
    return arr
    
arr = [963,5,34,254,23]
print(radix(arr))



