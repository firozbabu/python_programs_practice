
def partition(list,low,high):
    pivot = list[high]
    i = low-1
    for j in range(low,high):
        if list[j]<=pivot:
            i+=1
            list[i],list[j] = list[j],list[i]
            
    list[high],list[i+1] = list[i+1],list[high]
    return i+1




def quicksort(list,low,high):
    if low<high:
        index = partition(list,low,high)
        quicksort(list,low,index-1)
        quicksort(list,index+1,high)

list = [9,-3,5,2,6,8,-6,1,4]
quicksort(list,0,len(list)-1)
print(list)
