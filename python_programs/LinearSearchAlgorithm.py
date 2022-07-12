def linearsearch(array,element):
    for i in range(len(array)):
        if array[i]==element:
            return f"Element Found At Index {i}"
    return f'element not found'
print(linearsearch([1,2,3,4,5,6,7,8,9,10],10))
