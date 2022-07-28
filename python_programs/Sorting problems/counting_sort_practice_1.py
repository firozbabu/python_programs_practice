arr = [2,5,10,2,9,23,5,1,9,1,5,0,1]

#arr = [2,2,0,6,1,9,9,7]
max_el = max(arr)
count_array = [0]*(max_el+1)

for i in arr:
    count_array[i] += 1

for j in range(len(count_array)-2,-1,-1):
    count_array[j]+=count_array[j+1]

output_array  = [0]*len(arr)

i=0
while i<len(arr):
    current = arr[i]
    count_array[current]-=1
    output_array[count_array[current]]=current
    i +=1
print(output_array)
