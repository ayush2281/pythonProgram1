# the format() method formats the specified value(s) and insert the string's placeholder.
#the placeholder is defined using curly brackets {}. read more about the placeholder in the placeholder section below.

w = "Welcome {} to {} MyRepo".format("Hello",20)
print(w)

w = "Welcome {1} to {0} MyRrpo".format("Hello",20)
print(w)

# 10 is indiacating the 9 charcter space
w = "Welcome {a:10} to {b} MyRrpo".format(a=30,b=40)
print(w)

