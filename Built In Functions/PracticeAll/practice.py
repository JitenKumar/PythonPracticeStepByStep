# author : JitenKumar


from functools import reduce
# First


def digits_to_num(digits):
    return reduce(lambda x,y: x*10 + y,digits)


print(digits_to_num([3,4,3,2,1]))

# Second


def filter_words(word_list, letter):
    return list(filter(lambda x : x[0]==letter,word_list))


l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print(filter_words(l,'h'))

# Third


def concatenate(L1, L2, connector):
    return  [ x+connector+y for (x,y) in zip(L1,L2)]


print(concatenate(['A','B'],['a','b'],'-'))


# Fourth

def d_list(L):
    return {key: value for value, key in enumerate(L)}


print(d_list(['a','b','c']))

# Fifth


def count_match_index(L):
    return len([num for count, num in enumerate(L) if num == count])


print(count_match_index([0,2,2,1,5,5,6,10]))
