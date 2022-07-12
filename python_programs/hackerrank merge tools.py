'''
def merge_the_tools(string, k):
    # your code goes here
    p=[string[i:i+k] for i in range(0,len(string),k)]
    t=[]
    for i in p:
        r=[]
        for j in i:
            if j not in r:
                r.append(j)
        t.append(''.join(r))
    return '\n'.join(t)
a=input()
b=int(input())
print(merge_the_tools(a,b))
'''

'''

from itertools import permutations
a,b=input().split()
l=[''.join(i) for i in sorted(list(permutations(a,int(b))))]
print('\n'.join(l))
'''


from itertools import combinations

a,b=input().split()
l=[]
for i in range(1,int(b)+1):
    l+=sorted([''.join(i) for i in list(combinations(sorted(a),i ))])
    print(l)
print('\n'.join(l))
















