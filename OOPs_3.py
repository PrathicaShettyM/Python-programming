# Pillars of OOPs
'''
1. class
2. objects
3. inheritence
4. polymorphism
5. abstraction
6. encapsulation
'''

# Inheritence
# here 1 class inherits the properties of other class
# purpose of "super()" function: it calls the constructor of base class

class Parent:
    def __init__(self):
        self.super_attribute = True
        print("This is parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is the child class")
        print(self.super_attribute)
        
child1 = Child() 

'''
Types of inheritence
1. single inheritence
2. multiple inheritence

    class A:
    class B:
    class C(A,B):
    
3. multi level inheritence

    class A: 
    class B(A):
    class C(B):
    
4. heirarchical inheritence 

   class A:
   class B(A):
   class C(A):
   
5. Hybrid inheritence

    multi level inheritence + heirarchical inheritence + multiple inheritence
    class A:
    class B:
    class C(A,B):
    class D(C):
'''
# 1. vehicle parent, bus child. cost = seating_capacity*100, extra 10% on bus fare
class Vehicle:
    def __init__(self,seating_capacity): #constructor
        self.seating_capacity = seating_capacity
    def get_fare(self):
        return self.seating_capacity*100

class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)
        
    def get_fare(self): # if this is not called then parent get_fare() gets called
        vehicle_fare = super().get_fare()
        maintenance_fare = 0.10*vehicle_fare
        return vehicle_fare+maintenance_fare

vehicle1 = Vehicle(50) # initailise constructor
print("Vehicle fare:", vehicle1.get_fare())

bus1 = Bus(50) # initialise constructor
print("Bus fare:", bus1.get_fare())
        
        