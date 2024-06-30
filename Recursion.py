# Recursion:
# a function calling itself is called recursion

# 1. factorial question
def factorial(n):
    if n==0: # base case
        return 1
    return n*factorial(n-1) # recursive call

print("Factorial is:",factorial(5))

# 2. print numbers from N to 1
def print_n_to_one(n):
    if n == 0: # base case
        return
    print(n)
    print_n_to_one(n-1) # recursive call
print("Numbers from n to 1")
print_n_to_one(5)

# 3. print numbers from 1 to N
def print_one_to_n(n):
    if n==0: # base case
        return
    print_one_to_n(n-1) # recursive call
    print(n)
    
print("Numbers from 1 to n")
print_one_to_n(5)

# 4. Sum of 1 to n
def sum_of_1_to_n(n):
    if n == 1:
        return n
    return n+sum_of_1_to_n(n-1)

print("The sum of n numbers is:", sum_of_1_to_n(7))

# 5. 'a' raised to power 'b'
def exponent(a,b):
    if b == 0:
        return 1
    return a*exponent(a,b-1)

print("The ans of 5 raised to power 4 is: ", exponent(5,4))

# 6. Fibonacci series
def fibonacci(n):
    if(n <= 1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print("The 8th fibonacci number is:", fibonacci(8))
for i in range(1, 9):
    print(fibonacci(i))


