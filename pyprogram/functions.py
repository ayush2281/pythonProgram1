# A function is a block of statement which can be used repetively in a program> it saves
# the time of a developer. in python concept function is same as in other languages
# You can pass data, known as parameter, into a function

# in python a function is defined using the (def keywords)



#1 simple function
#2 function with arguements
# 3 return type

#1 simple function

#define
def showdata():
    print("hello coders")
#call
showdata()
showdata()
showdata()

#2 function with arguements

def sumdata(a,b):
    print(a+b)

n = 22
n1 = 25
sumdata(n,n1)

m = 512
m1 = 562
sumdata(m,m1)


#default arguements
def adddata(b,b1=20):
    print(b+b1)

adddata(5)

