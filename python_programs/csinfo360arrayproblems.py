#https://www.csinfo360.com/p/array-practice-problems.html


'''
#1. program to read and display the matrix

a,b = list(map(int,input().split()))
matrix = []
for i in range(a):
    matrix.append(list(map(int,input().split())))


for j in matrix:
    print(*j)
'''


'''      
#2. program to find the sum of all elements in 2d array

a,b = list(map(int,input().split()))
matrix = []
for i in range(a):
    matrix.append(list(map(int,input().split())))


s = 0
for j in matrix:
    for k in j:
        s +=k

print(s)
'''



#3. Addition of two matrices


a,b = list(map(int,input().split()))
first_matrix = []
second_matrix = []
for j in range(a):
        first_matrix.append(list(map(int,input().split())))

for k in range(a):
    second_matrix.append(list(map(int,input().split())))

sum_matrix = [[0 for i in range(b)] for l in range(b)]
for i in range(len(first_matrix)):
    for y in range(len(first_matrix[0])):
        sum_matrix[i][y] = first_matrix[i][y]+second_matrix[i][y]

print(sum_matrix)
