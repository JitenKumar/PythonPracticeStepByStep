# Dictionaries comprehensions
print({a:a**4 for a in range(10)})

d = {a:a*3 for a in range(4)}

for k in d.values():
    print(k)

for k in d.items():
    print(k)

for k in d.keys():
    print(k)

# viewing key and values

print(d.keys())



