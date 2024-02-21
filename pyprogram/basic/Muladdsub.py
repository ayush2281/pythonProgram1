# the value of this statement is
a=4*(6 + 5)

print(a)
b= (9*10) + 20-9.75
print(b)

c = 3+1.5+4
print(c)


# square root :
print(10 ** 2)

# string
s= 'Hello'
print(s[0])

# reverse string using slicing
s= 'Hello'
print(s[::-1])


# give the string hello , give the two mnethod of producing the letter 'o' using indexing
s= 'Hello'
#method 1
print(s[4])
#method 2
print(s[-1])

# Reassign 'hello' in this nested list to say 'goodbye' instead

list1 = [1,2,[3,4,'hello']]
list1[2][2] = 'goodbye'
print(list1)

# sort the list below:
list2 = [10,5,4,2,3,0,1]
#method1
print(sorted(list2))
#method2
list2.sort()
print(list2)

# dictionaries
#Grab hello anonymous
d = {'simple_key':'hello Anonymous'}
print(d['simple_key'])

d1 = {'k1':{'k2':'hello'}}
print(d1['k1']['k2'])

#grab helloman
#this is harder theb i excepted...
d2 = {'k1':[{'nest_key':['this is deep',['helloman']]}]}
print(d2['k1'][0]['nest_key'][1][0])


d3 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2['hello']]}]}]}
print(d3['k1'][2]['k2'][1]['tough'][2][0])