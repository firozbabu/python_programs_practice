#print('meme programmers')


a=[[1,2,3,4,5],[16,17,19,18,6],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
c=[]
while a:
    c.append(tuple(a.pop(0)))
    a=list(zip(*a))[::-1]
print(*sum(c,()),sep=' ')
    
