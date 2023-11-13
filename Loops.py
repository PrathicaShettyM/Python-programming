# for loop
# range (0, n-1) : 0 to n-1 and i = i+1

for i in range(0,10):
    print("Hello python",i)

# to increase the steps ex: i = i + 2
# range : `range(start, end-1, step)`
# if range(11) : then it will run from 0 to 11-1(10)

for i in range(0,10,2):
    print(i)

for _ in range(0,10,2):
    print("Hello world")

# print elements of a list using for loop
list1 = [10,20,30,40,50]
fruits = ["apples", "bananas", "cherry", "grapes", "mango"]

for i in list1:
    print(i) 
    
for i in fruits:
    print(i)

# While loop : runs till a condition is true
i = 0
while i<10:
        print("Hello programming world", i)
        i+=1
        
# PATTERN PRINTING
*****
*****
*****
n = int(input("Enter n : "))
for _ in range(n):
        print("*" * 5)

# 1234
# 1234
# 1234
# 1234
n = int(input("Enter n : "))
for i in range(n): #rows
    for j in range(1, n+1): #cols
        print(j, end="")
    print()

# 1
# 12
# 123
# 1234
n = int(input("Enter n : "))
for i in range(1, n+1): #rows
    for j in range(1, i+1): #cols
        print(j, end="")
    print()

#     1
#    123
#   12345
n = int(input("Enter n : "))
   
for i in range(1, n+1): #rows
    # spaces
    print(" " * (n-i), end="")
    for j in range(1, 2*i): #cols
           # digits
        print(j, end="")
    print()



