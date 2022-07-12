def atoi(s):
    t = ''.join(list(filter(None,s.strip('.'))))
    print(t)
    t = t.split(' ')
    print(t)
    e = 0
    if t[0].isalpha():
        return 0
    elif int(t[0]):
        e = int(t[0])
    minus = -2**31
    add = (2**31)-1
    if e<minus:
        return minus
    elif e>add:
        return add
    else:
        return e
s = '    -42'
print(atoi(s))
        
