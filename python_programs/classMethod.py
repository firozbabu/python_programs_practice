import datetime
class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age

    @classmethod
    def getAgeAsDob(cls,name,id,age):
        return cls(name,id,datetime.datetime.now().year-age)



student1 = Student.getAgeAsDob('Rakhi',1000001,2000)
print(student1.name,student1.id,student1.age)
student2 = Student('xyz',10831,21)
student3 = Student.getAgeAsDob('abc',25264,2001)
