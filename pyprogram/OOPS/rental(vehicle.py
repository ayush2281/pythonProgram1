#Bike rental system
# 1.display available
# 2.request a bike foe rent(100R->1qty)
# 3.Exit
class BikeShop:
    def __init__(self,stock): #create constructor
        self.stock=stock      #Variable
    def displayBike(self):
        print("total Bikes",self.stock)
    def rentForbike(self,q):
        if q<=0:
            print("Enter the positive value or greator then zero")
        elif q>self.stock:
            print("Enter the value (less then stock")
        else:
            self.stock=self.stock-q
            print("total prices",q*1000)
            print("total Bikes",self.stock)
while True:
    obj=BikeShop(100)
    uc=int(input('''
1 display Stocks
2 rent a bike
3 exit

            '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter the QTY.."))
        obj.rentForbike(n)
    else:
        break

