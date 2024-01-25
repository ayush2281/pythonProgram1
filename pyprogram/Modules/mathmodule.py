#MATH.CEIL(X)
#Return the ceiling of x, the smalllest integer greater than or equal to x. if x is not a float,
#delegate to x.__ceil__()which,should return an integral value.

# ceil --> it will give answer in int only suppose if you have 1.2 float num after you print you got 2

import math
x = 7.75
print(math.ceil(x))

#math.fabs --> Return thr absoulute value of x, return the positive value
x = -10
print(math.fabs(x))

#factorial--> retuen the x as an factorial integer, if you take x as negative you get error
x = 4
print(math.factorial(x))

# FLOOR--> Floor is reverse CEIL
x = 7.75
print(math.floor(x))

#MATH.FSUM(ITERATE)--> return a  accurate point sum of value in the iterable.

t = (6,5,9,80)
print(math.fsum(t))

#MATH.SQRT(X)
#return the square root of x
x = 36 # 36 is square root of 6
print(math.sqrt(x))



