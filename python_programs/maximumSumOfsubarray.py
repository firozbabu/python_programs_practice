p = [-1,-2,-3,-4]




'''
maxsub = 0
for i in range(len(p)):
    for j in range(i,len(p)):
        #subarray = 0
        for k in range(i,len(p)):
            #subarray += p[k]
            #print(sum(p[i:k]))


        if subarray>maxsub:
            maxsub  = subarray
print(maxsub)

'''

t = 0
for i in range(len(p)):
    sub = 0
    for j in range(i,len(p)):
            sub += p[j]
            if sub>t:
               t = sub
               print(t)
print(t)
            
