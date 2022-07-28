def countingforradix(inputarray,placevalue):

    countarray = [0]*10
    inputsize = len(inputarray)


    for i in range(inputsize):
        placeelement = (inputarray[i]//placevalue)%10
        countarray[placeelement] +=1


    for i in range(1,10):
        countarray[i] += countarray[i-1]


    outputarray = [0]*inputsize

    i = inputsize-1

    while i>=0:
        currentel = inputarray[i]
        placeelement = (inputarray[i]//placevalue)%10
        countarray[placeelement] -=1
        newposition = countarray[placeelement]
        outputarray[newposition] = currentel
        i-=1

    return outputarray


def radix(inputarray):

    maxel = max(inputarray)
    d = 1
    while maxel>0:
        maxel/=10
        d+=1


    placevalue = 1

    outputarray = inputarray

    while d>0:
        outputarray = countingforradix(outputarray,placevalue)
        placevalue*=10
        d-=1
    return outputarray


input = [963,5,34,254,23]
#input = [2,20,61 ,997,619]
#arr = [963,5,34,254,23]
print(input)
sorted = radix(input)
print(sorted)
