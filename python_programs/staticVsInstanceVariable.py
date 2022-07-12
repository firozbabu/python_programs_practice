class Student:

    def __init__(self, name, rollNo, address, phoneNo):
        self.name = name
        self.rollNo = rollNo
        self.address = address
        self.phoneNo = phoneNo
        self.schoolName = 'XYZ'

s1 = Student('A', 1, 'a', 2345678)
s2 = Student('B', 2, 'b', 2346678)
s3 = Student('C', 3, 'c', 2345678)
s4 = Student('D', 4, 'd', 6875648)



for obj in [s1,s2,s3,s4]:
    print(obj.name)
    print(obj.rollNo)
    print(obj.address)
    print(obj.phoneNo)
    print(obj.schoolName)
    
