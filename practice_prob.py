# WAP to check whether the number even or odd
class check_no:
    def even_odd(self,n):
        if self.n%2==0:
            print("The number is even")
        else:
            print("The number is odd")
num1=check_no()
num1.n=int(input("Enter the number:"))
# num1.even_odd(7)

# WAP in python to multiple two object using operator overloading
class demo:
    def __init__(self,x):
        self.x=x
    def __mul__(self,other):
        print("the value of object1 is:",self.x)
        print("the value of object2 is:",other.x)
        print("Multiplication of two numbers is:")
        return(self.x*other.x)
obj1=demo(10)
obj2=demo(20)
obj3=obj1*obj2
print(obj3)

# WAP to create a class with special overloaded operator for checking le
class demo:
    def __init__(self,x):
        self.x=x
    def __le__(self,other):
        print("the value of object1 is:",self.x)
        print("the value of object2 is:",other.x)
        print("The lower value of two number is:")
        return(self.x<=other.x)
obj1=demo(30)
obj2=demo(20)
obj3=obj1<=obj2
print(obj3)