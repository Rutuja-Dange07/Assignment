# 1. Write a password guessing program to keep track of how many times 
# the user has entered the password wrong. If it is more than 3 times, 
# print "You have been denied access." and terminate the program. If 
# the password is correct, print "You have successfully logged in." and 
# terminate the program.
psswrd="pass123"
n=0
while n<3:
  enter_passwrd=input("Enter the password: ")
  if enter_passwrd==psswrd:
    print("ACCEPT")
    break
  else:
    n+=1
    print(f"Incorrect password.You have {3-1} attempt")
if n==3:
  print("DENY")

# 3. Write a program to check whether the given string is palindrome or not
name=input("Enter a name:")
name1=""
for i in name:
  name1=i+name1
if name==name1:
  print("String is palindrome")
else:
  print("String is not palindrome")

# 5. Program to print a Fibonacci Series.
num=int(input("Enter number:"))
x,y=0,1
for i in range(num+1):
  z=x+y
  print(z)
  x,y=y,z

# 2. Write a program that asks for two numbers. If the sum of the numbers 
# is greater than 100, print "That is a big number" and terminate the 
# program.
num1=int(input("Enter th number:"))
num2=int(input("Enter th number:"))
sum=num1+num2
if sum>100:
    print("This is a big number")
else:
    print("This is a small number")

# 4. Write a program to calculate the BMI of a person
kg=int(input("enter the weight in kg:"))
meter=int(input("enter the height in meter:"))
bmi=kg/meter**2
print("BMI IS:",bmi)