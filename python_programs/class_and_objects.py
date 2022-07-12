class BankAccount:
    def __init__(self, accountNo, accountName, ifseCode, balance):
        self.accountNo = accountNo
        self.accountName = accountName
        self.ifseCode = ifseCode
        self.balance = balance
    def withdraw(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def checkBalance(self):
        print(self.balance)
   

object1 = BankAccount(12345678910,'dhoni', 'MPT10010122', 10000)
object2 = BankAccount(34424020480, 'virat', 'MPT10010122', 2000)
print(object1.accountName)
print(object2.accountName)


#object1.checkBalance()
#object1.deposit(5000)
#object1.checkBalance()
#object1.withdraw(2000)
#object1.checkBalance()
