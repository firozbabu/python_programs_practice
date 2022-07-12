class A:
    def __setitem__(self,attribute,value):
        print('setitem method called')

a = A()
a['m'] = 10
