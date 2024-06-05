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

# print elements of a list using for loop(buts prints everything in separate line)
list1 = [10,20,30,40,50]
fruits = ["apples", "bananas", "cherry", "grapes", "mango"]
clg = ["rvce", "bmsce", "msrit", "pesu"]

for i in list1:
    print(i) 
    
for i in fruits:
    print(i)
    
for i in clg:
    print(i)

# While loop : runs till a condition is true
i = 0
while i<5:
        print("Hello programming world", i)
        i+=1
        
# PATTERN PRINTING
# 1. *****
#    *****
#    *****
n = int(input("Enter n : "))
for _ in range(n):
        print("*" * 5)

# 2. 1234
#    1234
#    1234
#    1234
n = int(input("Enter n : "))
for i in range(n): #rows
    for j in range(1, n+1): #cols
        print(j, end="")
    print()

# 3. 1
#    12
#    123
#    1234
n = int(input("Enter n : "))
for i in range(1, n+1): #rows
    for j in range(1, i+1): #cols
        print(j, end="")
    print()

# 4.  1
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



