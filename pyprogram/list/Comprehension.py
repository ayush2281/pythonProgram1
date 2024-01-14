# list comprehension means compress of code
# list comprehension is elegant way to define create lists based on existing lists
# list comprehension is generally more  compact and faster than normal function and loops for

# normal function
# l = []
# for a in range(1,51):
#     # print(a)
#   l.append(a)
# print(l)
print("\n")

Comprehension
n = [h for h in range(1,51)]
print(n)

n = [h for h in range(1,51) if h%2==0] #even no
print(n)

m = [h for h in range(1,51) if h%2!=0] #odd number
print(m)

s = "Anonymous"
d = [g for g in s]
print(d)