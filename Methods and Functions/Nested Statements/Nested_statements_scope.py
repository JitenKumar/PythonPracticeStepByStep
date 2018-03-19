# LEGB RULE FOR THE SCOPES
# NESTED FUNCTIONS
name  = 'Global Jiten'
def first():
    name = 'Jiten'
    def second():
        print("name is"+name )
    second()
first()
print(name)

# global usage
x = 100

def func():
   # x= 200
    global x
    print(x)
    #Local change in the varible
    name = 'cool'
    x = 300
    print(name )
    print(x)
    # if want to acces the global and change it
print(x)
func()