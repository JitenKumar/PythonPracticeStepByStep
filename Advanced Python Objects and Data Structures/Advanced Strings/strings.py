st = 'jitender'
print(st.capitalize())
print(st.upper())
print(st.lower())
print(st.isalnum())
print(st.isalpha())
print(st.isupper())
print(st.isspace())
print(st.title())

# location and counting
print(st.count('i'))
#
print(st.find('j'))
print(st)


# Formatting the strings

print(st.center(20,'A'))

print('Jitender\tKumar'.expandtabs())
print(st.endswith('r'))
print(st.endswith('a'))

# Built in regular expressions

string = 'Hello this is the string'
print(string.split('e'))

string = 'Cool'
print(string.split('o'))

string  = 'This is the new awesome string and cool'
print(string.partition('o'))