


class NIT:
   def displayinfo(self):
       print("Welcome to NIT")
class IIT(NIT)  : # this is overriding
    def displayinfo(self):
        # super().displayinfo() # but if you want printf both use super func
        print("Welcome to IIT")

obj=IIT()  # this is overriding
obj.displayinfo()