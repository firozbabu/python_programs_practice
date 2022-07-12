



from random import randrange

'''
a = [1,2,3,4,5,6,7,8,9,0]
print(a)
for i in range(len(a)):
    j = randrange(i+1)
    a[i],a[j] = a[j],a[i]
print(a)
'''


k = int(input())
cards = [i for i in range(1,53)]
for i in range(k):
    j = randrange(1,k)-1
    cards[i],cards[j] = cards[j],cards[i]
print(cards)
