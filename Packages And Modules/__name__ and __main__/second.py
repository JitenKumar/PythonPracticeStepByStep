import first

print('top inside the second.py')

first.func()

if __name__ == '__main__':
    print('second is being executed directly')
else:
    print('second is being imported')

# inside the terminal run
# python first.py and then
# python second.py