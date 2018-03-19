class Dog():
    def __init__(self,name):
        self.name= name
    def speak(self):
        print("Woof my name is {}".format(self.name))

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("meow my name is {}".format(self.name))


niko = Dog('niko')
isis = Cat('isis')
print(niko.speak())
print(isis.speak())
niko.speak()

# Abstract class
class Animal():
    def __init__(self):
        print('Animal')
    def speak(self):
        raise NotImplementedError('Subclass must implement this method')

class Dog(Animal):
    def __init__(self,name):
        print('Dog created')
        self.name = name
    def speak(self):
        print('woof my name is {}'.format(self.name))
doggy = Dog('Jimmy')
print(doggy.speak())
