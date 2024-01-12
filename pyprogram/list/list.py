
# List --> Mutable data types
#  list is and ordered sequnces of items.
l=[1,2.2,'as']
l[0]=60 # it add the number in list on place of 0.
print(l,type(l))
print(l[1]) # it will give indivisual number on the place 1
print(l[0:2])

l1=[2,3,"Hello",2,3,3.2]
print(l1,type(l1))
# print(l1)
print(l1[0:2]) # 2 se ek kam chalega
print(l1[0:])  # it will give whole list
print(l1[3:])  # it will give whole list

print("\n")
print("Increment of two,two")
l2=[1,2,3,5,6,7,9]
print(l2)
print(l2[-1::-1]) # reverse of list numbers
print(l2[0::2]) # output  1,3,6,9
print(l2[-1::-1-1]) # increment of two number Output : 9,6,3,1
