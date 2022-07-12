class Calculator:

    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b

    @staticmethod
    def mul(a,b):
        return a*b

    @staticmethod
    def div(a,b):
        return a/b

calculator1 = Calculator()
print(calculator1.add(10,20))
print(calculator1.sub(15,2))
print(calculator1.mul(3,11))
print(calculator1.div(30,5))
