# This is a single comment
''' This is a multiline comment'''

print("Hello python")
print(3+4)

a = 20
b = 34
sum = a+b
print(sum)

ch_1 = 'a'
str = "string"
print(type(ch_1))
print(type(str))

dec_num = 8.90
print(dec_num)

bool_val = True
print(bool_val)

print(dec_num, bool_val)

# print variable in sentences
name = "Ironman"
age = 20
power = 92.57
active = True
print("This is " + name)
print("This is " + name + " whose age is", age, "and come with the strength of",power," and it is", active)

print('this is a single quote string')

# ord: character to ascii
# chr: ascii to character
ch_2 = 'p'
print(ord(ch_2))

ch_3 = 97
print(chr(ch_3))

# note: here '/' means complete division, whereas '//' means division in case of c, cpp, java
print("Addition:", 5+3)
print("Subtraction:", 5-3)
print("Multiplication:", 2*3)
print("Division:", 5/3)
print("Modulo:", 5%3)
print("Exponentiation:", 5**3)
print("Floor division:", 5//3)

exp_1 = 1 >= 2   # false
exp_2 = 3 > 2    # true
print(exp_1 and exp_2) # false 
print(exp_1 or exp_2)  # true
print(not exp_2)       # false

india = 5
australia = 3
print(india is not australia)
print(india is australia)

print("Membership operators")

python_lists = ["fruits", "veggies", "nuts", "meat"]
print("nuts" in python_lists)
print("salad" not in python_lists)

a = 5
b = 3
print(a ^ b)
print(a & b)
print(a | b)

# area of sphere
'''
radius = int(input("Enter the radius: "))
volume_of_sphere = (4/3)*3.1415*(radius**3)
print("The volume of the sphere is: ", volume_of_sphere)
'''

# typecasting
a1 = 10
b1 = 20
c1 = 30
flt_1 = float(b1)
print(flt_1)

# deg c to deg f
'''degree_celsius = float(input("Enter the temperature in degree celsius: "))
degree_fahrenheit = (9/5)*degree_celsius + 32
print("The converted temperature is: ", degree_fahrenheit)'''

# conditional statements
''' if, else, elif and ladder'''
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1 > num2:
    print(num1,"is greater than",num2)
elif num1 == num2:
    print("Both", num1,"and", num2,"are equal")
else:
    print(num2,"is greater than", num1)
'''

''' match case: calculator '''
'''
op1 = int(input("Enter 1st number: "))
op2 = int(input("Enter 2nd number: "))
op = (input("Enter the operator: "))

match op:
    case "+": 
        print("Sum is:", op1+op2)
    case "-":
        print("Difference is:", op1-op2)
    case "*":
        print("Product is:", op1*op2)
    case "/":
        print("Quotient is:", op1/op2)
    case _ :
        print("Enter a valid operator")
'''
       
''' ternary operator '''
output = "Even" if 6%2==0 else "Odd"
print(output)
    


