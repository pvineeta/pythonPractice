# class - collection of objects or blue print for creating objects.

'''
how to define a class

class ClassName:
    objects1
    objects2
    .
    .
    objectsN

Note:
class is a keyword
what comes next to class keyword is class name
'''
###################################################
#
#
#
#
#
###################################################
# write a class which have two objects/methods where in first method takes 2 args and return some of those
# and another method takes three arguments and returm multiplication of those

class Calc:
    def sum(self, a, b):
        return a + b
    def mul(self, a, b, c):
        return a * b * c
# here is the challange to call or access sum and mul
# i.e you need to create an object of class Calc to access these methods

# create an object of class
# self is a positionl args and it has to pass with every method

vin = Calc();
print(vin.sum(10, 20))
