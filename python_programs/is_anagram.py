str1  = input().lower()
str2 = input().lower()
s1 = {}
s2 = {}
for i in str1:
    if i in s1:
        s1[i]+=1
    else:
        s1[i]=1

for i in str2:
    if i in s2:
        s2[i]+=1
    else:
        s2[i]=1

print(s1==s2)
