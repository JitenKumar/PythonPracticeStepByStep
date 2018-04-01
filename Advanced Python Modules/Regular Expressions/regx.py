import re
# searching for patters in a string
patterns = ['first1', 'first2']
text = 'this is a string with the first1 and first2'
for pattern in patterns:
    # check for match
    print(' Searching for  {} in {}'.format(pattern, text))
    if re.search(pattern, text):
        print('Match Found')
    else:
        print('No Match found')

'''
.search() will take the pattern, scan the text,
 and then return a Match object. If no pattern is found, None is returned.
'''
match = re.search('jiten','jitender is here you can search him')
print(type(match))  # <class '_sre.SRE_Match'> returned
# show start if match
print(match.start())
# show end of match
print(match.end())

# Split with regular expressions¶
split_text = '#'
text = "Today's most searched hashtag is #BumShiva"
print(re.split(split_text, text))

# FINDING ALL INSTANCES OF A PATTERS
print(re.findall('jitender','jitender was here and jitender went left to his home a few moments earlier'))

# Repetition Syntax

'''
* : a patter followed by "*"  is repeated zero or more times
+ : a pattern followed by "+" is repeated 1 or more times
? : a patter followed by  "?" is repeated o or 1 times
{m}: For a specific number of occurrences, use {m} after the pattern,
      where m is replaced with the number of times the pattern should repeat.
{m,n}: Use {m,n} where m is the minimum number of repetitions and n is the maximum.
     Leaving out n {m,} means the value appears at least m times, with no maximum
'''
# function to find multi


def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')

# examples


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_pat = [ 'sd*',             # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]
multi_re_find(test_pat, test_phrase)

# CHARACTER SETS

test_text = 'ksjhnfiuwr8ii1j0pkofifknslkmflskjbkslmvlsnvjksml;v,snriushewionfvlskmvshjhjkhjsfhsjhjhkjkjhkjhkh'
test_pt = ['[jk]','h[jk]+']
multi_re_find(test_pt,test_text)

# EXCLUSION
# We can use ^ to exclude terms by incorporating it
#
# into the bracket syntax notation. For example: [^...] will match any single
# character not in the brackets.
t_text = 'This is a string! but it has punctuations? , fjsk'
print(re.findall('[^!.? ]+',t_text))

#character ranges
test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns = ['[a-z]+',  # sequences of lower case letters
                 '[A-Z]+',  # sequences of upper case letters
                 '[a-zA-Z]+',  # sequences of lower or upper case letters
                 '[A-Z][a-z]+']  # one upper case letter followed by lower case letters

multi_re_find(test_patterns, test_phrase)


# ESCAPE CODES

test_phrase = 'This is a string with some numbers 1233ab , 242 3552,672462842,8274 and a symbol #hashtag ,$0928402'
test_patr = [ r'\d+',   # seq of digits
              r'\D+',   # seq of non digits
              r'\s+',   # seq of whitespaces
              r'\S+',   # seq of non whitespaces
              r'\w+',   # seq of alphanumeric
              r'\W+',   # seq of non-alphanumeric
              ]
multi_re_find(test_patr, test_phrase)







