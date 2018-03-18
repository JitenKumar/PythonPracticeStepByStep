# class for user defined objects
class Sample():
    # Class Object attributes
    # will be same for every instance
    species ='Homo Sapiens'
    def __init__(self,name,lastame,hobbies,age):
        self.my_name = name
        self.last_name = lastame
        self.my_hobbies = hobbies
        self.my_age = age


my_obj = Sample('jiten','palsra','cricket',20)
print(my_obj.my_name)
print(my_obj.species)
print(my_obj.last_name)
print(my_obj.my_hobbies)
print(my_obj.my_age)

# Another example


class Circle():
    pi = 3.14

    def __init__(self,rad=1):
        self.radi = rad
        self.area = self.radi**2 * Circle.pi

    def get_circumference(self):
        return self.radi * self.pi *2

crc = Circle(30)
print(crc.radi)
crc.radi = 30
print(crc.area)