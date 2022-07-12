'''
s = 'This1 is0 me3 and my5 friend2'
s = s.split(' ')
c=[ 0 for i in range(20)]
for i in s:
    for j in i:
        if j.isdigit():
            c[int(j)]=i
print(' '.join(c))
            
'''

A = [10,2,5]
B=[40,90,20]
C=[3,5,4]
count=0
total = 0
for i in range(len(C)):
    for j in range(len(A)):
        if C[i]>=A[j]:
            count+=1
            total+=B[j]
            B.pop(j)
            A.pop(j)
            break
return '









            
            
