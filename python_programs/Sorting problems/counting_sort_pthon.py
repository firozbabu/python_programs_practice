def countingSort(inputarray):
    maxElement = max(inputarray)
    countarraylength = maxElement+1
    countarray = [0]*countarraylength

    for el in inputarray:
        countarray[el] +=1

    for i in range(1,countarraylength):
        countarray[i] += countarray[i-1]

    outputarray = [0]*len(inputarray)
    i = len(inputarray)-1

    while i>=0:
        currentEl = inputarray[i]
        countarray[currentEl] -= 1
        newposition = countarray[currentEl]
        outputarray[newposition] = currentEl
        i-=1

    return outputarray


inputarray = [2,2,0,54,234,656,23,-454,-11,88]
print(countingSort(inputarray))
