# Encapsulation : An object should not always be directly accessible.
# (Encapsulation is made for private uses)
# the methods can ensure the correct values are set.if am incorrect value is set, the method can return erroe
# Getter and setter : getter and setter is not inbuilt function this taken by user

class Student:
    __name="Ayush"  #private vector is made by (__)underscore,underscore
    def __init__(self):
        print(self.__name)
        self.__titlename()
    def __titlename(self):
        print("Hello Coders")
obj= Student()






