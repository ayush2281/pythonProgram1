# Mutable and Immutable data type
# Mutable -->  Jismein hum changes kar paye wo mutablde
# Immutable -->  Jismein hum changes na kar paye wo Immutablde

#   Mutable Data Types: |   #   ImMutable Data Types:
#   list                |  Number --> int , float , complex ,
#   dictionary          |        string
#   byte array          |        Tupple , sets

#int
a = 5
print(a,type(a))

#float
a = 2.2
print(a,type(a))

#complex
a = 2+5j
print(a,type(a))

#string
b = "Anonymous is good coder@1366"
print(b,type(b))
b = '''
         hii
     Please save me...
'''
print(b)
b = '10'
print(b,type(b))

#set
# is an unordered collection of list
#Every set element is unique(no duplicates) and must be immutable (can't be changed)
my_set = {2,3,75,65}
print(my_set,type(my_set))

# Tupple
# tupple is an ordered sequences of items same as a list
# it is defined within parenthesis () where items are seprated by commas
t = (96,3,'hello')
print(t,type(t))

# List --> Mutable data types
#  list is and ordered sequnces of items.
l=[1,2.2,'as']
l[0]=60
print(l,type(l))

#dictionary
# dictionary is an unordered collection of key-values pairs.
#  in python , dictionaries are defined  within breaces{} with each items being pair in the form key:values

d ={
    'intern_name': 'Google',
    'intern_duration':'45 Days'
}
print(d['intern_name'])
print(d,type(d))

d2 = {
    'job_profile': 'software engineer'
    'job_duration':'45 months'

print(d2['job_profile'])
print(d2, type(d2))



}

