

#oneway

a = input()
b = input()


#print(bin(int(a,2)+int(b,2))[2:])



#another way


res = ''
carry = 0
sum = 0


if len(a) > len(b):
    b = '0'*len(a)-len(b)+a
else:
    a = '0'*len(b)-len(a)+b

print(a,b)
