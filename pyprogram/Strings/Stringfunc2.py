                        # Strings Function
   # find() , index() , isalpha() ,  isdigit() , isalnum()

#find
# in the find if we put non given character it will give you answer in -1
z = "Make You Strong"
print(z.find('z'))  # OT  -> 3
print(z.find('o',2))  # the mean of 2 is start from 2 index

#index
#  in the index if we put non given value it will give you error
# print(z.index('z'))

#isalpha --> isalpha means all alphabates
a = "Anonymous123"
print(a.isalpha()) # output : it includes only alphabates

# isdigit() it include only number
n = "123"
print(n.isdigit())  # true
# isalnum --> it include both alphates and number but dont use special char like @,#,$,&
r = "Anonymous126"
print(r.isalnum())

