program 1:-syntax
print("this is my first python program")


program 2:- Identation
if 5 > 2:
  print("Five is greater than two!")


program 3:- indentation with 2 block of codes
if 5>3:
    print ("5 is greater than 3")

    if 5<6:
        print ("5 is less than 6")
else:
    print("statement is false")


program 4:- Identation should be same in the same blcok of code else it will throw error.
if 5>3:
    print ("5 is greater than 3")
    print ("5 is less than 6")


program 5:- variables
x = 100
y = "hello"
print (x)
print (y)


program 6:- write a method which takes two arguments and return sum of those
def sum(a, b):
    c = a + b
    return c # return is a keyword which override the default return property of a function

x  = sum(6, 5)
print(x)


program 7:- write another method which takes two arguments and return multiplication of those
#define/declaritive
def mul(a,b,c):
    d = a * b * c
    return d
    print('Hello')

# calling
x = mul(10, 2 , 5)
print(x)


program 8:- write a class which have two objects/methods where in first method takes 2 args and return some of those
and another method takes three arguments and returm multiplication of those

class Calc:
    def sum(self, a, b):
        return a + b
    def mul(self, a, b, c):
        return a * b * c

vin = Calc();
print(vin.sum(10, 20))


program 9:- Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

vin = Person("vineeta" , 30)
print(vin.name)
print(vin.age)


program 10:- Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return ("my name is " + self.name)

p1 = Person("vineeta")
print(p1.greet())


program 11:-  simple program to retun values

class A:
    def m(self, b):
        self.b = b
        return b + 5
    def p(self, c):
        return self.b + c


program 12:- sum & multiplication program with __init__

class Calci:
    def __init__(self, a, b, c):
        ## pass
        self.a =  a
        self.b = b
        self.c = c
    def sum(self):
        return self.a + self.b
    def mul(self):
        return self.a * self.b * self.c

vin = Calci(4, 6, 7)
print(vin.sum())
print(vin.mul())
