# iterate over 2+ lists at the same time (zip function)
l =[20,90,70,46]
l1 =[9,5,8,1]
t = len(l)

for a,b in zip(l,l1):
    print(a,b)

# 2nd method
for h in range(t):
    print(l[h],l1[h])
