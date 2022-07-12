class A:
    __a = 10
    ___b = 20
    ____c = 30
    _____d = 40
    __e_  = 50
    __f__ = 60
    __g___ = 80
    ___h_ = 90
    _i_ = 100
    ___j___ = 200

    def getPrivateData(self):
        print(self.__a)


class B(A):
    def getPrivateMember(self):
        print(self._A__a)

obj1 = A()
print(obj1._A__a)
obj2 = B()
obj2.getPrivateMember()
print(obj2._A__a)
