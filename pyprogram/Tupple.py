# Tupple
# tupple is an ordered sequences of items same as a list
# it is defined within parenthesis () where items are seprated by commas
#tupple iterations
# t = (96,3,'hello')
# print(t,type(t))
# a=t[1]
# print(a,type(a))
#
# # method1
# l =len(t)
# for a in range(l):
#     print(t[a])
# # method
# for a in t:
#     print(a)


    # Now Come to tupple functions
#  min(), max() , count() index() , sum()

#min
t = (30,5,40)
m = min(t)
print(m)
#count
c = t.count(40)
print(c)

#index
i = t.index(5)
print(i)

#max
m2 = max(t)
print(m2)

#sum

s = sum(t,10) #if you want to add anynumber in number pass(,and any number)
print(s)










