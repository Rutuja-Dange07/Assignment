# 1. Write a Program to create a class by name Students, and initialize 
# attributes like name, age, and grade while creating an object. 
class Students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Grade:",self.grade)
obj1=Students("RUTUJA",20,10)
obj1.display()


# 2. Write a program, to create a child class Teacher that will inherit the 
# properties of Parent class Staff. 
class Staff:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Teacher(Staff):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
    def display(self):
        super().display()
        print("Department:",self.dept)
obj1=Teacher("Manoj",20,"IT")
obj1.display()


# 3. Write a Program, to create class and using the class instance print all 
# the writable attributes of that object. 
class Instances:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)
obj1=Instances("John",21,2000000)
obj1.display()

        

# 4.reate a class Teacher with name, age, and salary attributes, where 
# salary must be a private attribute that cannot be accessed outside 
# the class
class Teacher:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary=salary                            # private method
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

    # get_salary() is a public method
    def get_salary(self):
        return self.__salary

obj1=Teacher("Manoj",20,200000)
obj1.display()
print("Salary:",obj1.get_salary())


# 5.Write a Python program that overloads the operator + and > for a 
# custom class. 
class demo:
    def __init__(self,x):
        self.x=x
    def __gt__(self,other):
        print("The lower value of two number is:")
        return(self.x>other.x)
    
    def __add__(self,other):
        print("The Addition of two number is:")
        return(self.x+other.x)

obj1=demo(1)
obj2=demo(2)
obj3=obj1>obj2
print(obj3)

obj1=demo(1)
obj2=demo(2)
obj3=obj1+obj2
print(obj3)


# 6. Write a Python class Square, and define two methods that return the 
# square area and perimeter.
class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return self.side * 4
s = Square(5)
print("Area:",s.area())
print("Perimeter:",s.perimeter())
