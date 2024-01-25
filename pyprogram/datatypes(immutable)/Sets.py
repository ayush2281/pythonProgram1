#set
# is an unordered collection of list
#Every set element is unique(no duplicates) and must be immutable (can't be changed)
s = {2,75,3,65}
print(s,type(s))

# iterate in set
for a in s:
    print(a)


    #sets functions
 # set() , add() , pop() , remove() , clear() , discarsd() , update()

# convert list into set
l =[2,6,58,7]
# s = set(l)
print(set(l))

# add
s = {2,9,8,4,6}
s.add(65)
print(s)

# pop() : it will delete the random element
p ={6,3,10}
p.pop()
print(p)

#remove : Note :
r = {130,60,50}
r.remove(130)
print(r)

#discard--> Note: if the item to remove doesn't exist , discard() will not raise an error
d = {130,60,50}
d.discard(60)
print(d)

#clear

c = {76,1.1,63}
c.clear()
print(c)

#update : it will help to update multiple elements

l2=[50,9,4,30]
u ={30,40,60}
u.update(l2)
print(u)
