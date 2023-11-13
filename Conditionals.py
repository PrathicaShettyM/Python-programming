# take input, tell if the integer is positive or negative
n = int(input("Enter a no. : "))
if n >= 0:
    print("The no. is positive")
else:
    print("The no. is negative")
    
take input and tell odd or even
n = int(input("Enter a no. : "))
if n % 2 == 0:
    print("The no. is Even")
else:
    print("The no. is Odd")

# take sp and cp, tell profit or loss, and calculate profit or loss
cp = int(input("Enter the cost price of the item : "))
sp = int(input("Enter the selling price of the item : "))
if cp == sp:
    print("No profit, No loss")
elif sp > cp:
    print("profit")
    profit = sp-cp
    print("The profit is : ", profit)
else:
    print("loss")
    loss = cp - sp
    print("The loss is : ", loss)

# grade card
marks = int(input("Enter the marks of the student : "))
if (marks>81) and (marks<=100):
    print("Very good")
elif (marks>61) and (marks<=80):
    print("Good")
elif (marks>41) and (marks<=60):
    print("Average")
else:
    print("Fail")

# greatest of 3 no.s using "nested if else"
a = int(input("Enter 1st no. :"))
b = int(input("Enter 2nd no. :"))
c = int(input("Enter 3rd no. :"))

if a > b:
    if a > c:
        print("\'a\' is greatest")
    else:
        print("\'c\' is greatest")
else:
    if b > c:
        print("\'b\' is greatest")
    else:
        print("\'c\' is greatest")

# take an integer input and telll if it is divisible by 5 or 3 but not divisible by 15
n = int(input("Enter a positive no. :"))
if n % 15 == 0: 
    print("The no. is divisible by 15")
else:
    if (n % 3 == 0) or (n % 5 == 0):
        print("Number is not divisible by 15, but divisible by either 3 or 5")
    else:
        print("The no. is not divisible by both 3 and 5")


# MATCH CASE(similar to switch case in cpp and java)

calculator using match case
num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))

operator = input("Enter an operator :")

match operator:
    case "+":
        print("The sum is :", num1+num2)
    case "-":
        print("The difference is :", num1-num2)
    case "*":
        print("The product is :", num1*num2)
    case "/":
        print("The quotient is :", num1/num2)
    case _ :
        print("Enter a valid operator")

# ternary operator
# odd or even using ternary operator
num = int(input("Enter a number: "))
 
output = "Even" if num%2==0 else "Odd"
print("Output is : ",output)

