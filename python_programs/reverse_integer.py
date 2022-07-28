def reverse(x):
        s = str(x)
        if x<0:
            t = s[0]+s[len(s):0:-1]
        else:
            t = s[::-1]
            if t[0]=='0':
                t=t[1:]
        if int(t)>(2**31)-1:
            print(0)
        elif int(t)<(-2**31):
            print(0)
        else:
            print(int(t))

for i in range(3):
    x = int(input())
    reverse(x)
