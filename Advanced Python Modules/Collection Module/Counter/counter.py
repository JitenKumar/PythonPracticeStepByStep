'''

The collections module is a built-in module that implements specialized container
data types providing alternatives to Python’s general purpose built-in containers

'''
from collections import Counter
list = [62.874,2,14,4,3546,6,24,1,1,1,4,674,5,3,53,54,3]
# it will give me a dict of count of all elements

print(Counter(list))

# Counter with the strings
print(Counter('khsfygwifuhnwlfjpwkfijfls;v,s'))

# counter on string containing words

string = 'this is the most common string in the python and counter is going to count how many times a word appeared '
c = Counter(string.split())
print(c)
# most common  in the string
print(c.most_common(2))
print(c.values())

# list of unique elements
# print(list(c))
# convert to a set
st = set(c)
print(st)
#
print(c.items())
# print(Counter(dict[c.items()]))