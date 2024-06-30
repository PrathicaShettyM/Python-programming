# Functions:
# a block of reusable code which performs a specific task
# types: built and user defined

def hello():
    print("Hello python")

hello()

# types of arguements
# positional arguement
def add(n1, n2): # these are parameters
    sum = n1+n2
    return sum

x = 5
y = 7
print("The sum is: ", add(x,y)) # pass arguements
print("another sum is: ", add(3,9)) # positional arguements

# keyword arguements(named arguement)
print("one more sum is: ", add(n2=2,n1=4)) # here order doesnt matter, name matters

# default arguement
def add2(n1, n2=0):
    return n1+n2

print("The (default arg) sum is: ", add2(5))

# arbitrary arguement(variable length arguements *args and *kwargs
'''
*args
def addAllNumbers(*args):
    # args -> tuple
'''
def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

output = addAllNumbers(1,0,9,8,3,5,7)
print("The sum is : ", output)

'''
**kwargs: keyword arguement for key value pairs -> dictionary
 **kwargs -> will be passed as a dictionary
'''
def student_Info(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)
        
        
student_Info(name="Prathica", age=20, city="Bangalore")
print()
student_Info(name="Rohit", age=37, city="Mumbai")
print()
# scope of function call
# always call the function after it is declared and defined

def sumOfOneToN(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

# n = int(input("Enter n: "))
# print("Finally the sum is:", sumOfOneToN(n))

# nested functions
def outerfunction():
    x = 5
    def innerfunction():
        y = 3
        return x+y
    return innerfunction()

print("Result: ",outerfunction())
print()

# PASS BY VALUE and PASS BY REFERENCE

# 1. Pass by value (This is for immutable objects like strings,integers,float,tuple)
'''
When these are passed to a function a copy of the object is created and is assigned to the local variable in the 
function
Any changes made to them inside function, do not affect the original value outside the function
'''

def addOne(x):
    x += 1
    print("Inside function: ",x)

x = 5
print("Outside function: ", x)
addOne(x)
    
# 2. Pass by reference (This is for mutable object - lists, dictionaries)
'''
Reference to actual object is passed to function
changes in function will affect the original object as well
'''
def modifyList(lst):
    lst.append(4)
    lst = [4,5,6]
    print("Inside the function: ",lst)
    
lst = [1,2,3]
modifyList(lst)
print("Outside function: ", lst)
    
# Built in function
# 1. factorial of a number

def factorial(n):
    ans = 1
    if n == 0:
        return ans
    else:
        for i in range(1,n+1):
            ans *= i
    return ans

n = int(input("Enter a number n: "))
print("Factorial:", factorial(n))













