arr = list(map(int,input().split()))
length = len(arr)
result = [1 for _ in range(length)]

print(result)

prod = 1
for i in range(length):
    result[i] *= prod
    prod *= arr[i]

    print('inside first for loop',result)
    print('inside first for loop',prod)

print(result)
prod = 1
for i in range(length-1,-1,-1):
    result[i]*=prod
    prod*=arr[i]
    print('inside second for loop',result)
    print('inside second for loop',prod)
print(result)
