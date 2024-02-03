# Encapsulation : An object should not always be directly accessible.
# (Encapsulation is made for private uses)
# the methods can ensure the correct values are set.if am incorrect value is set, the method can return erroe
# Getter and setter : getter and setter is not inbuilt function this taken by user
import self


class Student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name



obj=Student()
obj.setname("Testing")
name=obj.getname()
print(name)