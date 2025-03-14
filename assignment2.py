# 1.WAP to calculate the simple interest
def simple_int(p,r,t):
     s=(p*r*t)/100
     print("SIMPLE INTEREST IS:",s)
simple_int(10000,5,3)

# 2.WAP to calculate compound interest
def compound_int(p,r,t):
    c=p*(1+r/100)**t-p
    print("COMPOUND INTEREST IS:",c)
compound_int(25000,10,2)

# 3.WAP to check the given year is a leap year or not
yr=int(input("ENTER THE YEAR: "))
if yr%4==0:
    print("LEAP YEAR")
else:
    print("NOT LEAP YEAR")

# 4.Take the input from the user that is age and check eligibility for voting or not
age=int(input("ENTER THE AGE: "))
if age>18:
    print("ELIGIBLE FOR VOTING")
else:
    print("NOT ELIGIBLE FOR VOTING")

# 5.Design the simple calculator using if-elif-else statement
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
else:
    print("Invalid operator!")