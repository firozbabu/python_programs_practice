
text = "....  and so on ...."
y = text.split()

j = 1

for i in y:
    if i.isalpha():
        t = i
        break

r = t[0]
while j<len(t):
    if r[-1].isalpha() and t[j].isalpha() or t[j]=="'":
        r+=t[j]
        j+=1
    elif r[-1] == "'" and t[j].isalpha():
        r+=t[j]
        j+=1
print(r)
