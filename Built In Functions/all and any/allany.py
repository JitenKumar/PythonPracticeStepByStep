# all() and any() are built-in functions in Python that allow us to
# conveniently check for boolean matching in an iterable. all()
#  will return True if all elements in an iterable are True

list = [True,False,True,False]
print(all(list))
print(any(list))

list1  = [1>3,3>5,7>6]
print(all(list1))
print(any(list1))