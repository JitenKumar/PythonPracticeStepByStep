l1 = [1,2,34,5,6]
l2 = [3,3,2,1,34,5]
zp = zip(l1,l2)
print([x for x in zp])

list_a = [1,2,3434,3]
list_b = [84.4245,535,3545,3]

print(list(zip(list_a,list_b)))

# zip with the map function
print(list(map(lambda x: max(x),zip(list_a,list_b))))
# zip with the dictionaries
dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}

def func_switch(d1,d2):
    dres = {}
    for d1key,d2value in zip(d1,d2.values()):
        dres[d1key] = d2value
    return dres

print(func_switch(dict1,dict2))
