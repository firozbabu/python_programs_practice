#1st way

l = [0,1]
for i in range(2,19):
    l.append(l[-1]+l[-2])
print(l)

#1st  way find nth fibonacci

import decimal
decimal.Decimal().prec = 10000

