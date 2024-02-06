#Bike rental system
# 1.display available
# 2.request a bike foe rent(100R->1qty)
# 3.Exit
class BikeShop:
    def __init__(self,stock): #constructor
        self.stock=stock
    def displayBike(self):
        print("total Bikes",self.stock)
    def rentForbike(self,q):
        if q<=0:
            print("Enter the positive value or grator than zero")
        elif q>self:
            print("Enter thr the value (less then stock")
        else:
            print("total prices",q*100)
            print("total Bikes",self.stock)
while True:
    uc=int("in")

