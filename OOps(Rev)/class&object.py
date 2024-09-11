#creating class
# class Student:
#     name = 'Ayush'
#     roll_no = 230
#     specialization = "Ai"



#creating object (instance)

# s1 = Student()
# print(s1 )
# print(s1.name)
# print(s1.roll_no)
# print(s1.specialization)

# class Container:
#     size = '320*170'
#     color = "blue"
#     price = 175000
#     charges = 50000
#     time = "2 days"
#
# b2 = Container()
#
# print(b2.price)
# print(b2.size)
# print(b2.color)
# print(b2.time)
# print(b2.charges)


#constructor
# All classes have function called __init__(), which is always executed when the object is being initiated.

# class Student:
      #default constructor
#     def __init__(self,name):
#         parameterized constructor
#         self.name = name
#         print("adding new student in section")
#
# s1 = Student('ayush')
# print(s1.name)
#

# class Agency:
#     def __init__(self, finance, sex):
#         self.finance = finance
#         self.sex = sex
#
#
# DC = Agency("420", 'male' )
# print(DC.finance)
# print(DC.sex)


class University:
    college_name = 'Mit'
    def __init__(self,No_of_students , fee, year, rollno):

        self.No_of_students = No_of_students
        self.fee = fee
        self.year = year
        self.rollno = rollno
    def welcome(self):  #methods
        print('Welcome Students',self.fee)

aktu = University('120 Students','165000/yr',"4-Years", "230")
aktu.welcome()
print(aktu.college_name)
print(aktu.No_of_students)
print(aktu.fee)
print(aktu.year)
print(aktu.rollno)





































