#1.There are 5280 feet in a mile. 
# Write a Python statement that calculates and prints the 
# number of feet in 13 miles
mile=5280
feet=13
print(mile*feet)

#2.Write a Python statement that calculates and 
# prints the number of seconds in 7 hours, 21 
# minutes and 37 seconds.
hour=7
min=21
sec=37
print(hour*60*60+21*60+37)

#3.The perimeter of a rectangle is 2w+2h, 
# where w and h are the lengths of its sides. Write a 
# Python statement that calculates and 
# prints the length in inches of the perimeter of a 
# rectangle with sides of length 4 and 7 inches. 
w=4
h=7
p=2*w+2*h
print("perimeter of area is:",p)

#4.The circumference of a circle is 2πr where r is the radius of the circle. Write a Python 
# statement that calculates and prints the circumference in inches of a circle whose radius is 8 
# inches. Assume that the constant π=3.14
rad=8
c=2*3.14*8
print("circumference is:",c)

# 6.Write a Python expression that combines the string “SDP Guruji is 27 years old." from the 
# string “SDP Guruji" and the number 27 and then prints the result.  
str1="SDP Guruji is "
num=str(27)
str2=" years old"
print(str1+num+str2)

#7.Write a single Python statement that combines the three strings "My name is", “SDP" and 
# “GURUJI" (plus a couple of other small strings) into one larger string "My name is SDP 
# GURUJI." and prints the result.  
print("My name is"+" "+"SDP"+" "+"GURUJI")


# 8.The distance between two points (x0, y0) and (x1, y1) is 
# (x0−x1)2+(y0−y1)2. Write a Python 
# statement that calculates and prints 
# the distance between the points (2,2) and (5,6). 
distance=(2-5)**2+(2-6)**2
print(distance)