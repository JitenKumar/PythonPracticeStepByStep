# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if
# both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5
def lesser_of_two_evens(a,b):
    if a<b:
        return a
    else: return b
print(lesser_of_two_evens(2,4))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(text):
    wordlist = text.lower()
    wordlist = wordlist.split()
    return wordlist[0][0] == wordlist[1][0]

animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')

# MAKES TWENTY: Given two integers, return True if the sum of
# the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20

makes_twenty(20, 10)
makes_twenty(12, 8)
makes_twenty(2, 3)

# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald


def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    first_half.capitalize()
    second_half.capitalize()
    return first_half + second_half


old_macdonald('macdonald')

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'


def master_yoda(text):
    mylist = text.split()
    #backward
    mylist= mylist[::-1]
    return ' '.join(mylist)


# Check
master_yoda('I am home')


# LEVEL 2 PROBLEMS
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False


def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


# Check
has_33([1, 3, 3])


# Check
has_33([1, 3, 1, 3])


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(text):
    res = ''
    for ch in text:
        res += ch*3
    return res


# Check
paper_doll('Hello')


# BLACKJACK: Given three integers between 1 and 11, if
# their sum is less than or equal to 21, return their sum. If
# their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a, b, c):
    sm = a + b + c
    if sm <= 21:
        return sm
    elif sm > 21 and 11 in [a, b, c]:
        return sm - 10
    else:
        return 'BUST'


# Check
blackjack(5,6,7)


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections o
# f numbers starting with a 6 and extending to the next 9 (every 6 will be
#  followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    total = 0
    # boolean to check for addition
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
                break
        while not add:
            if num != 9:
                add = False
                break
            else:
                add = True
                break
    return total


# Check
summer_69([2, 1, 6, 9, 11])


#
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

# first solution if code contains them in order next to each other
def spy_game(nums):
    length = len(nums)
    res = False
    for i in range(0, length):
        if i <= length - 3:
            if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
                res = True
    return res


# if contain it in any order

def spy_game1(nums):
    cd = [0,0,7,'j']
    for num in nums:
        if num == cd[0]:
            cd.pop(0)
    return len(cd) == 1
