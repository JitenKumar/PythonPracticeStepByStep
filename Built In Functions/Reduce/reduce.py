# we will find the smallest no in python using the reduce
from functools import reduce
list =[1,42,42,235,464,64,3424,46352,424.424,2424]
# first way
min_no = lambda x,y: x if(x<y) else y
res = reduce(min_no,list)
print(res)

# second way directly print it
print((reduce(lambda x,y: x if(x<y) else y,list)))