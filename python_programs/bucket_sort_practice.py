def insertion_sort(array):
    for j in range(len(array)):
        index = j
        while index>0 and array[index]>array[index-1]:
            array[index],array[index-1] = array[index-1],array[index]
            index-=1
            

arr = [2,5,10,2,9,23,5,1,9,1,5,0,1]
max_el = max(arr)
size = max_el/len(arr)
buckets = [[] for i in range(len(arr))]


for i in range(len(arr)):
    j = int(arr[i]/size)
    if j!=len(arr):
        buckets[j].append(arr[i])
    else:
        buckets[len(arr)-1].append(arr[i])

for x in range(len(arr)):
    insertion_sort(buckets[x])

output = []
for i in range(len(arr)-1,-1,-1):
    output += buckets[i]

print(output)
