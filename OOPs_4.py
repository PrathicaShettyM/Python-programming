# POLYMORPHISM(poly="many" morphism="forms")
# It allows objects of different classes to behave as objects of the same superclass
 
class Animal:
    def speaks(self):
        pass
    
class Dog(Animal):
    def speaks(self):
        print("Bark")
        
class Cat(Animal):
    def speaks(self):
        print("Meow")
        
class Cow(Animal):
    def speaks(self):
        print("Moo")
# create objets
dog = Dog()
cat = Cat()
cow = Cow()
# call the methods
dog.speaks()
cat.speaks()
cow.speaks()

# polymorphism is of 2 types
# 1. compile time polymorphism: decided at compile time which version of the function will be invoked
#    compile time polymorphism is achieved through:
#    a. method overloading
class Add:
    def sum(self, a, b):
        print(a+b)
    def sum(self, a, b, c): #only this recent one will be called
        print(a+b+c)

ans = Add()
ans.sum(4,5,3)

#    b. operator overloading 
class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def __add__(self, other):
        return ComplexNumber(self.real+other.real, self.img+other.img)

c1 = ComplexNumber(1,2)
c2 = ComplexNumber(3,4)
c3 = c1+c2
print(c3.real, "+ i", c3.img)
    
# 2. run time polymorphism: decided at run time which version of the function will be invoked
#    achieved through method overriding
# same as the animal class example above

# ABSTRACTION
# allows us to focus on the 'what' of an object rather than 'how' of an object
# abstracts the unnecessary complexity from the end user
# ann abstract class may contain abstract methods, which must be implemented by its concrete subclass

# ENCAPSULATION
# bundles the attributes(details) and the methods(functions) together in one entity -> class

# Exception Handling
'''
try
    # code which might throw an error
except
    # code to handle exception
    # handles exception of the following types: 
    # value error
    # type error
    # zero division error
    # exception
finally
    # executed regardless of exception
''' 

# 2. exception handling division by zero

a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    result = a/b
except ZeroDivisionError:
    result = None
    print("Error: cannot divide by zero")
finally:
    print("Division operation completed: ", result)    



