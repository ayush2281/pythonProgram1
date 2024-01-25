#method 1
# import module1
# print(module1.sum(10,20))
# print(module1.mul(10,20))

#method 2
# import module1 as m
# print(m.sum(10,20))
# print(m.mul(10,20))


#method3
#for indivisual function
from module1 import sum
print(sum(9,5))

#for all function use(*) keyword

from module1 import *
print(sum(9,5))
print(mul(9,5))


