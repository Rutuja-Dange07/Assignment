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