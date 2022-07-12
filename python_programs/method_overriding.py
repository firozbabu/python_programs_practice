class Mobile:
    def __init__(self, price, modelNo):
        self.price = price
        self.modelNo = modelNo
    def discountPrice(self):
        return self.price-self.price*(1/10)
    def commonmethod1(self):
        return 'this is common method1'
    def commonmethod2(self):
        return 'this is common method2'
    def getPrice(self):
        return self.price
    def getModel(self):
        return self.modelNo

class Iphone(Mobile):
    def __init__(self, price, modelNo):
        Mobile.__init__(self, price, modelNo)
    def somemethod1(self):
        return 'this is some method1'
    def somemethod2(self):
        return 'this is some method2'
    def discountPrice(self):
        return self.price - self.price*(15/100)

class Samsung(Mobile):
    def __init__(self, price, modelNo):
        Mobile.__init__(self, price, modelNo)
    def somemethod3(self):
        return 'this is some method3'
    def somemethod4(self):
        return 'this is some method4'

class Sony(Mobile):
    def __init__(self, price, modelNo):
        Mobile.__init__(self, price, modelNo)
    def somemethod5(self):
        return 'this is some method5'
    def somemethod6(self):
        return 'this is some method6'

class RedMe(Mobile):
    def __init__(self, price, modelNo):
        Mobile.__init__(self, price, modelNo)
    def somemethod7(self):
        return 'this is some method7'
    def somemethod8(self):
        return 'this is some method8'


iphone_object1 = Iphone(50000,10001)
print(iphone_object1.discountPrice())
samsung_object1 = Samsung(50000,10101)
print(samsung_object1.discountPrice())
