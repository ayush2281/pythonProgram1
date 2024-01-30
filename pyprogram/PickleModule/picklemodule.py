# the pickle module implements a fundamental, but powerful algorithm for serializing
#  and de-serializing a python object structre
      # Storing data with pickle
# 1 - Booleans , 2 - integers 3- floats 4- complx number 5- (normal and unicode)String
# 6- Tuples 7-lists 8-sets and 9 - Dictionaries


import pickle
# dump()- the function is called to serialize an object hierarchy.
# load() - this function ic called to de-serialize a data stream

# 1-
l = [3,60,36,97]
file=open("writedata.txt","wb")
pickle.dump(l,file)
file.close()