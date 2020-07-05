'''
class Calci:
    def __init__(self, a, b, c):
        ## pass  # if you want to keep this method without any statement
        self.a =  a
        self.b = b
        self.c = c
    def sum(self):
        return self.a + self.b
    def mul(self):
        return self.a * self.b * self.c

vin = Calci(4, 6, 7) # __init__ gets invokded when class being initialized
print(vin.sum())
print(vin.mul())
'''
# sum and mul are public method so they are accessible from out side of the class
# in python private method start with __ and end with __

'''
class A:
    def m(self, b):
        self.b = b
        return b + 5
    def p(self, c):
        return self.b + c

Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

vin = Person("vineeta" , 30)
print(vin.name)
print(vin.age)

Insert a function that prints a greeting, and execute it on the p1 object:
'''
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return ("my name is " + self.name)

p1 = Person("vineeta")
print(p1.greet())
