           # Method Overring
#it is use for inhertance(merging).
#method overriding is the methof having the same name with same arguments.
#it is mosty used for memory reducing process.

class C:
    def showData(self):
        print("I am in C section ")
class D(C):
    def showData(self):
        print("I am in D section ")

obj = D()
obj.showData()