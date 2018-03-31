def func(num):
    return num ** 4
lst = [1,2,3,4,5]

print(list(map(func,lst)))
# map with multiple iterables
list_a = [1,3,5,6,5]
list_b = [3,5,6,7,8]
list_c = [8,3,1,2,43]
var_z = map(lambda x,y,z: x + y + z , list_a, list_b, list_c)
var_mul = map(lambda i,j,k: i*j*k ,list_a, list_b, list_c)
print(list(var_z))
print(list(var_mul))