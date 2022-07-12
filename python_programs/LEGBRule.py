'''
class Account:
    def __init__(self,acno,acname,acntbal):
        self.acno = acno
        self.acname = acname
        self.acntbal = acntbal

class AccountDemo:
    def __init__(self):
        pass

    def depositAmnt(self,acnt,depamnt):
        acnt.acntbal += depamnt
        return acnt.acntbal
    
    def withdrawAmnt(self,acnt,withamnt):
        if acnt.acntbal - withamnt >=1000:
            acnt.acntbal-=withamnt
            return acnt.acntbal
        else:
            return 'No Adequate balance'


if __name__ == '__main__':
    acno = int(input())
    acname = input()
    acntbal = int(input())
    depamnt = int(input())
    withamnt = int(input())
    acnt = Account(acno,acname,acntbal)
    acntdemoobj = AccountDemo()
    print(acntdemoobj.depositAmnt(acnt,depamnt))
    print(acntdemoobj.withdrawAmnt(acnt,withamnt))
'''




'''


p=[]
for i in a1:
    if (i in a2) and (i in a3):
        p.append(i)
return *sorted(p)
'''
'''

a = input()
p = 0
for i in range(1,len(a)+1):
    for j in range(len(a)-i+1):
        p+=int(a[j:j+i])
print(p)
'''
'''
number = int(input('Enter the number: '))
if number%3==0 and number%5==0:
    print('FizzBuzz')
elif number%3==0:
    print('FIzz')
elif number%5==0:
    print('Buzz')
else:
    print(number)
'''

'''
gender = 'male'
age = 10
if gender=='male' and age<30:
    print('30 below male')

'''
''''

for i in range(50):
    print(i)
    print('Meme programmers')


'''

'''

class SampleClass:
    pass


def vLKA(**k):
    return k
print(vLKA(a=1,b=2))

'''
'''
print((lambda marks: 'excellent' if marks>90 else ( 'good' if marks>70 else ( 'average' if marks>60 else 'fail')))(75))

def grade(marks):
    if marks>90:
        return 'excellent'
    elif marks>70:
        return 'good'
    elif marks>60:
        return 'average'
    else:
        return 'fail'
print(grade(75))
'''



'''
a = 10
def sampleFunction():
    a = 20
sampleFunction()
a = 30
print(a)

'''





































