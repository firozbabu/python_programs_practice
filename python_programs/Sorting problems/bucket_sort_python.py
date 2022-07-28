def insertion(bucket):
    for i in range(1,len(bucket)):
        j = i
        while j>0 and bucket[j]<bucket[j-1]:
            bucket[j],bucket[j-1] = bucket[j-1],bucket[j]
            j-=1




def bucket_sort(arr):

    max_value = max(arr)
    size = len(arr)/max_value
    print(size)
    buckets = [[] for i in range(len(arr))]

    for i in range(len(arr)):
        j = int(arr[i]/size)
        print(j)
        if j!=len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr)-1].append(arr[i])


    print(buckets)
    for x in buckets:
        insertion(x)

    print(buckets)
    final_list = []
    for i in buckets:
        final_list+=i

    return final_list

print(bucket_sort([7, 6, 5, 4, 3, 2, 1]))
