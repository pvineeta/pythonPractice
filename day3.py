# write a python class which contains 1 method which takes 1 argument & return the type of an object.

class Person:
    def __init__(self, b):
        self.b = b

    def my_fun(self, a):
        return type(a)

vin = Person('ds')
print(vin.my_fun(4))
