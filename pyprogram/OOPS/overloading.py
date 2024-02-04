              # method Overloading
# Method overloading is on concept of polymorphism.
#it comes under the element of OOPs.
#it is wprked in the same method names and different arguments.
#Arguments different will be based on number of arguments and the types of arguments.


class Area:
    def find_area(self,m=None,n=None):
        if m!=None and n!=None:
            print("area of rec", m*n)
        elif m!=None:
            print("Square of M",m*m)
        else:
            print("Nothing to find ")
obj= Area()
obj.find_area() # it will give you nothing beacause you pass nothing
obj.find_area(10) # it will pass second cond
obj.find_area(10,20) # 1st condition beacause you pass two variable
