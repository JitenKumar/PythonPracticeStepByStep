'''

The main difference is when a generator function is compiled they become an object that supports an iteration protocol.
That means when they are called in your code they don't actually return a value and then exit. Instead,
 generator functions will automatically suspend and resume their execution and state around the last point of value
 generation. The main advantage here is that instead of having to compute an entire series of values up front,the generator computes one
 value and then suspends its activity awaiting the next instruction. This feature is known as state suspension.

'''


def square(n):
    for x in range(n):
        yield x ** 2


for num in square(5):
    print(num)


# FIBONACCI EXAMPLES

def fibo(n):
    first = 0
    second = 1
    for i in range(n):
        yield first
        first, second = second, first + second


for x in fibo(10):
    print(x)

# using next() and iter()

def simple(n):
    for x in range(n):
        yield x


sm = simple(4)
print(next(sm))
print(next(sm))
print(next(sm))
print(next(sm))


for let in 'JITENDER':
    print(let)
# this will give an error
#print(next('HELLO'))

sm_itr = iter('JITENDER')
print(next(sm_itr))


# Generator comprehensions
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)