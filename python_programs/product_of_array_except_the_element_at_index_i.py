#given an array of integers return a new array such that
#each element at index of the new array is the product of
#all the numbers in the original array except the one at i

list = [1,2,3,4,5]
p = []
for i in range(len(list)):
    prod = 1
    for j in range(len(list)):
            prod *= list[j]
    p.append(prod//list[i])
print(p)
