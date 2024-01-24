# what are function and methods in python
# get() , key s() ,  values() , iems()


d = {
    'course': 'python',
    'fees': 8000,
    'duration': '2Months'
}
#get()
n = d.get("course")
print(n)

#direct()
print(d['course'])

# it will print name
for c in d.keys():
    print(c)

# it will print value
for b in d.values():
    print(b)
#and it will print both
for n in d.items():
    print(n)

# delete keys
del d['fees']
print(d)

#pop

print(d.pop('duration'))
print(d)









