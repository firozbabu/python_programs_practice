#bit manipulation csinfo360.com


#problem-1

#find nth bit of a number

number = int(input())
pos = int(input())

res = bin(number)[2:]
print(res[pos])
