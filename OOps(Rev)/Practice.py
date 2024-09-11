#lets practice 1--->
# create student class thats takes name & marks of 3 subjects as arguments in constructor
# then create an method to print an avg

# class Students(): # class
#
#     def __init__(self,name, marks):
#         self.name = name
#         self.marks = marks
#
#
#     def get_avg(self): # method
#         sum = 0
#         for value in self.marks:
#             sum += value
#         print("Hi", self.name, " your avg score is:", sum/3)
#
#
# s1 = Students('Ayush',[98,99,82])
# s1.name = "tony stark"
# s1.get_avg()
#



# static method
#
# class Student()
#     @staticmethod




#lets practice --> 2
# create Account class with 2 attributes -balance & account no.
# creater an method for debit,credit & printing the blance


class Account():
    def __init__(self, balance , account_no):
        self.balance = balance
        self.account_no = account_no
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balnce is ", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance +=  amount
        print("Rs", amount, "was credited")
        print("total balnce is ",self.get_balance())

    # balance  method
    def get_balance(self):
        return self.balance


acc1 = Account(25000,54655268655644)
print(acc1.balance)
print(acc1.account_no)

acc1.debit(10000)
acc1.credit(5000)
acc1.get_balance(ba)
