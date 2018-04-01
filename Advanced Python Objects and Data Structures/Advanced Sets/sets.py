st = {1,3,4,4,3,3}
# will remove the extras

print(st)
# ADDING THE VALUES
st.add(124)
st.add(544)
print(st)

# CLEAR
# deleting the values
st.clear()
print(st)
st = {1,35,5545,353,535}
# COPY
s2 = st.copy()
print(s2)

s2.add(1)
s2.add(6868)
print(s2)
print(st)

# DIFFERENCE
print(s2.difference(st))
print(s2.difference_update(st))
print(st)
print(s2)

# discard
print(s2.discard(6868))
print(s2)

# Itersection

s = {1,2,34,5,5,6}
s2 = {1,4,57,5,5,6,464}
print(s.intersection(s2))
# intersection_update
# will update a set with the
# intersection of itself and another.
print(s.intersection_update(s2))
print(s)
print(s2)

# disjoints

s3 = {64,13,4244,5,535,6}
s4 = {64,8724,424,4,35,46}
print(s3.isdisjoint(s4))
s2 = {64}
# subset
print(s2.issubset(s4))

# print(s4.isupperset(s2))

# symmetric difference

print(s2.symmetric_difference(s4))
print(s3.symmetric_difference_update(s4))

print(s3.union(s4))

print(s2.update(s4))
print(s2)