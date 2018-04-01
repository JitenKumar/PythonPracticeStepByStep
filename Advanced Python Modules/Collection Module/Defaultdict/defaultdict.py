'''
defaultdict is a dictionary-like object which provides all methods provided by a dictionary but takes a first argument
(default_factory) as a default data type for the dictionary.
using default dict is faster than using the same as dict.set_default methods
'''
from collections import defaultdict
# normal dictionary

d = {'k1':1}
print(d['k1'])  # will print 1
# print(d['k2'])   will give an KeyError

# using the default dict


dct = defaultdict(object)   # takes an object
print(dct['k1']) # will give location and type as object

for it in dct:
    print(it)   # will print the key

dict2 = defaultdict(lambda: 1)
print(dict2['4'])    # will print 1

dict2['k2'] = 4
print(dict2['k2'])  # will print 4


