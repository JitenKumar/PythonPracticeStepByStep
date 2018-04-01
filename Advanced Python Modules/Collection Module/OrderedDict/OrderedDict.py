'''
An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
'''
from collections import OrderedDict
# normal dict is a mapping
print('Normal dictionary:')

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

# OrderedDict
print('OrderedDictionary')

d = OrderedDict()

d['k1'] = 'a'
d['k2'] = 'b'
d['k3'] = 'c'

for k,v in d.items():
    print(k, v)

# checking the equlity
d = OrderedDict()
d['k1'] = 'a'
d['k2'] = 'b'
d['k3'] = 'c'
d2 = OrderedDict()
d2['k1'] = 'a'
d2['k3'] = 'c'
d2['k2'] = 'b'

print(d == d2)  # will print false