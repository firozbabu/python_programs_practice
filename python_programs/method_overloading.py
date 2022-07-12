class A:
    def add(self,*args):
        if args:
            sum = type(args[0])()
            for i in args:
                sum+=i
            return sum

obj = A()

print(obj.add(1,2))
print(obj.add(1,2,3))
print(obj.add('a','b','c'))
print(obj.add('a','b'))
print(obj.add(12.3,3.42,4.56))
print(obj.add([1,2],[3,4]))
print(obj.add(1,2,4.5,6.7))
