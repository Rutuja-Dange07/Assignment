# WAP to check whether the number even or odd
class check_no:
    def even_odd(self,n):
        if self.n%2==0:
            print("The number is even")
        else:
            print("The number is odd")
num1=check_no()
num1.n=int(input("Enter the number:"))
num1.even_odd(7)

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

# WAP to create the class shape having same method and argument using method overlaoding
class shape:
    def show(self):
        print("hello")
class rectangle(shape):
    def show(self):
        super().show()
        print("world")
obj=rectangle()
obj.show()

# WAP to create,read and remove the existing file
f=open("file.text","w")
f.write("hello")
f.close()
f=open("file.text","r")
f.read()
f.close()
import os
os.remove("file.txt")


# WAP to check a specific condition that should raise an exception whenever you are enter the number 5
def inp():
    x=int(input("ENTER THE NUMBER:"))
    if x==5:
        raise ValueError
    return x
inp()
print("5 is bad number")


try:
    name=input("Enter the name:")
    year_born=input("Enter the year you born:")
    age=2025 - int(year_born)
    print("Your age is",age)
except TypeError:
    print("Typevalue occured")
except ValueError:
    print("Typerror occured")
except ZeroDivisionError:
    print("zeroDivision occured")
finally:
    print("This is finally block")


# create a list and raise the exception
list=[1,2,3,4,5]
if list[5]==5:
    raise Exception

# WAP to check whether the number even or odd
class check_no:
    def even_odd(self,n):
        if self.n%2==0:
            print("The number is even")
        else:
            print("The number is odd")
num1=check_no()
num1.n=int(input("Enter the number:"))                                    # jar ka he statement execute  karayche asel tr jo function use krt aahe tyala self. ni lihaych
num1.even_odd(7)


# WAP to create the student data entry in GUI
import tkinter                        
from tkinter import *                     
root=tkinter.Tk() 

l1=Label(root,text="student name:")              
l1.pack(side=LEFT)  

e1=Entry(root)                               
e1.pack(side=LEFT)

b1=Button(root,text="submit")                                      
b1.pack(side=LEFT)

l2=Label(root,text="student roll number:")              
l2.pack(side=RIGHT) 

e2=Entry(root)                               
e2.pack(side=RIGHT)

b2=Button(root,text="submit")                                      
b2.pack(side=RIGHT)

root.mainloop()    


# Create the student form using radio and check button
import tkinter
from tkinter import *
root=tkinter.Tk()

checkvar1=StringVar()
checkvar2=StringVar()
checkvar3=StringVar()
var=StringVar()

cb1=Checkbutton(root,text="Amravati")
cb1.pack()

cb2=Checkbutton(root,text="Mumbai")
cb2.pack()

rb1=Radiobutton(root,text="male",value="male")
rb1.pack()

rb2=Radiobutton(root,text="female",value="female")
rb2.pack()

lb1=Label(root)
lb1.pack()

root.mainloop()