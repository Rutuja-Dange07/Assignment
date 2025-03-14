# 1.print all numbers between 1 to 1000 which is divisible by 9 or must not be divisible by 3
for num in range(1,1000):
    if num%9==0 or num%3!=0:
      print(num)

# 2.calculate the square of a given number
num=int(input("ENTER NUMBER: "))
square=num**2
print(f"SQUARE OF {num} IS",square)

# 3.WAP to check whether the given number is prime number or not
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("not a prime number.")
            break
    else:
        print("prime number")
else:
    print("not a prime number.")

# WAP to convert temp from celsius to fahrenheit
temp=int(input("Enter the number:"))
fahrenheit=temp*(9/5)+32
print(fahrenheit)

# WAP to convert temp from fahrenheit to celsius
temp=int(input("Enter the number:"))
celsius=(temp-32)*(5/9)
print(celsius)