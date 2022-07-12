a = 'abcdefghjklmnopqrstuvwxyz'

def fun(i):
    if i not in 'aeiou':
        return True

result = filter(fun, a)
print(list(result))
