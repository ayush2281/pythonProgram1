# merging is called inheritance
class A:
    def displayA(self):
        print("Welcome to the page  A")
class B:
    def displayB(self):
        print("Hello Coders B")

#Multiple Inheritance
class C(A,B):
    def displayC(self):
        print("Welcome to page C")

obj=C()
# obj=B()
obj.displayA()
obj.displayB()
obj.displayC()