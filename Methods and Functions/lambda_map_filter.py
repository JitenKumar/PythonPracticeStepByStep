# lambda , map and filter practice

def square(nums):
    return nums ** 2
ls = [1,2,3, 4, 5]
for items in map(square,ls):
    print(items)
# getting back the list
print(list(map(square,ls)))

# FILTER RETURN TRUE OR FALSE FOR SOME FUNCTION
def check_even(nums):
    return nums%2==0
num = [1,2,3,4,5]
for items in filter(check_even,num):
    print(items)

# Lambda Expressions called as anonymous functions
# using in the map function
numbers = [1,2,34,345,6,4]
print(list(map(lambda num: num**2,numbers)))

# using with the filter function
names  = ['Jitender','Andy']
print(list(filter(lambda num:num%2==0,numbers)))
print(list(map(lambda x:x[::-1],names)))