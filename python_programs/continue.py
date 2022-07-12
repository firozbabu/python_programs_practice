p=[]
for i in a1:
    if (i in a2) and (i in a3):
        p.append(i)
return *sorted(p)


a = input()
p = 0
for i in range(1,len(a)+1):
    for j in range(len(a)-i+1):
        p+=int(a[j:j+i])
print(p)


number = int(input('Enter the number: '))
if number%3==0 and number%5==0:
    print('FizzBuzz')
elif number%3==0:
    print('FIzz')
elif number%5==0:
    print('Buzz')
else:
    print(number)


gender = 'male'
age = 10
if gender=='male' and age<30:
    print('30 below male')

for i in range(50):
    print(i)
    print('Meme programmers')


n=2
i=0
while i<10:
    if n%2==0 and n%7==0:
        print(n)
        i+=1
    n+=1

listOfStrings = ['tic','toc','toe']
for i in listOfStrings:
    for j in i:
        if j != 't':
            print(j)
