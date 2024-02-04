# Polymorphism means same function name (but different signature) being uses for different types
# different signature means -> like list,tupple,string

class As:
   def displayinfo(selfself,name=''):
       print("hello coders"+name)
obj=As()
obj.displayinfo()
obj.displayinfo(' Python') # overloading