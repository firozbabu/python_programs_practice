def bucket_sort(list):

    max_value = max(list)
    size = max_value/len(list)

    buckets_list = [[] for i in range(len(list))]

    for i in range(len(list)):
        j = int(list[i]/size)
        if j!= len(list):
            buckets_list[j].append(list[i])
        else:
            buckets_list[len(list)-1].append(list[i])


    print(buckets_list)
    for z in range(len(list)):
        insertion_sort(buckets_list[z])


    final_output = []
    for x in range(len(list)):
        final_output+=buckets_list[x]

    return final_output


def insertion_sort(bucket):
    for i in range(1,len(bucket)):
        var = bucket[i]
        j = i-1
        while j>=0 and var<bucket[j]:
            bucket[j+1] = bucket[j]
            j-=1
        bucket[j+1] = var


list = [2,43,6,0,9,3,4,1,9,0,1,5,2,29,85,12]
print(list)
print('after sorting',bucket_sort(list))
