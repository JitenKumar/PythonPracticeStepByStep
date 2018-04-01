l = [1,1,2,3,45,56]
# append
l.append(12)
l.count(3)
print(l.append([1,24,424]))
print(l)

# extends
l2 =[]
l2.extend([1,'13',4])
print(l2)

# count

print(l.count(1))

# index
print(l.index(1))

# insert
l.insert(1,4444)
print(l)

# pop
l.pop()
print(l)
print(l.pop(1))

# remove

l.remove(1)
print(l)

# reverse
l.reverse()
print(l)

# sort
l.sort()
print(l)

# common list assignment problems
y = l.append(1)
# list append is in place
print(y)
y = l.copy()
y.append(131313)
print(y)
