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


def bankCode(bal):
      inp = input()
      if not inp:
          return bal
      else:
          t,a = inp.split()
          if t=='D':
               bal+=int(a)
          else:
               bal-=int(a)
      return bankCode(bal)
print(bankCode(0))
'''

import time
print('fdfhdkhfdkhfd',end='')
time.sleep(5)
print('rturytiurytiurytiu,')

