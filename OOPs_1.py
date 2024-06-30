# Object Oriented Programming
# part 1
'''
POP vs OOP
In Procedure Oriented Programming, the main focus is on writing functions
In Object Oriented Programming, the main focus is on objects/data
'''

'''
Use of OOPs:
1. helps to mimic real world entities and their interactions
2. code reusability
3. organisation and maintainability of code
'''

'''
CLASSES:
1. user defined data types
2. blueprint / template for an object

OBJECT
1. is an instance of class
2. it mimics real-world entities
'''

'''
class car:
    # attributes: properties
    length
    color
    # methods: functions associated with the class
    get_fuel()
    start()
    stop()
object1 = car()

'''
# create a class Student
class Student:
    
    def set_name(self, name):
        self.name = name # class attribute
        
    def get_name(self):
        return self.name
# self is passed by default to all methods
# used to refer to the particular method and use the value passed to the method 
# create objects of class Student
student1 = Student()

# class methods
student1.set_name("Prathica") # object1
print(student1.name)
print(student1.get_name())
student1.maths_mark = 100
print(student1.maths_mark) # instance attribute

student2 = Student() # object2
student2.set_name("Ram")
print(student2.get_name())

# 1. Reactangle dimensions, area, perimeter
class Rectangle:   
    def __init__(self, height, width):
        print(f"A rectangle is created with height {height} and width {width}")
        self.height = height
        self.width = width
    
    # def set_dimensions(self, height, width):
    #     self.height = height
    #     self.width = width
        
    def area(self):
        return self.height*self.width
    
    def perimeter(self):
        return 2*(self.height+self.width)

rect1 = Rectangle(4,3) # goes to constructor and initialises it
rect2 = Rectangle(5,6)
rect3 = Rectangle(7,8)
# rect1.set_dimensions(10, 20)
# print("The height is:", rect1.height, "The width is:", rect1.width)
# print("Area is:", rect1.area())
# print("Perimeter is:", rect1.perimeter())

# constructor
'''
- it is a special function that gets invoked everytime an object is created for that class
- syntax:
    def __init__(self, param1, param2):
        # initalise variables
- refer the above example
- every time a new object is created the constructor is invoked
'''

# attributes
'''
2 types: 

1. class attributes
2. instance attributes

1. class attributes:
    - defined inside the class
    - all object instances will have these attributes
    
2. instance attributes:
    - are specific to a particular instance/object
'''









