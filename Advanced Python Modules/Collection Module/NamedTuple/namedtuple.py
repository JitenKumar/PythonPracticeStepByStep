# normal tuple
from collections import namedtuple
tp = (1,2,34,5,6)
print(tp[1])

'''
Each kind of namedtuple is represented by its own class, 
created by using the namedtuple() factory function. 
The arguments are the name of the new class and a string containing the names of the elements.

You can basically think of namedtuples as a 
very quick way of creating a new object/class type with some attribute fields.
'''

t = namedtuple('Human', 'name age gender maritalstatus')
jitender = t('jitender', 22, 'male', 'Single')
print(jitender)
print(jitender.name)
print(jitender.maritalstatus)
print(jitender.age)
print(jitender.gender)