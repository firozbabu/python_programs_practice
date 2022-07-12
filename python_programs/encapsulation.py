class Parent:
    __privateData = 10
    def publicMethod(self):
        print(self.__privateData)
class Child(Parent):
    def method(self):
        print(self.__privateData)



obj1 = Parent()
obj1.publicMethod()
obj2 = Child()
obj2.method()

