# Access modifiers:
# they are used to control the visibilty of class attributes and functions

# 1. public: accessible outside the class also
class Class1:
    def __init__(self):
        print("Inside public constructor")
        self.public_attribute = None # public attribute 
    
    def public_function(): # public function
        pass
obj1 = Class1()

# 2. private: not accessible outside the class
class Class2:
    def __init__(self):
        print("Inside private constructor")
        self.__private_attribute = None # private attribute 
    
    def __public_function(): # private function
        pass
obj2 = Class2()
# print(obj2.__private_attribute) # throws an error as private attribute is not accessible outside the class
# print(obj2.__private_function) # throws an error as private function is not accessible outside the class

# 3. protected: accessible outside the class to a subclass which has inherited some of the properties of the parent class
class Class3:
    def __init__(self):
        print("Inside protected constructor")
        self._protected_attribute = None # protected attribute 
    
    def _protected_function(): # protected function
        pass
obj3 = Class3()

