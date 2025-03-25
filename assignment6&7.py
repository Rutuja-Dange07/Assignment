# Q1. Creation of list and changing value of any one element, also display the length of list.
list=[1,2,3,4,5]
list[2]=6
print(list)
print(len(list))

# Q2. Create a list and append two elements in it. 
list=[1,2,3,4]
list.append(5)
list.append(6)
print(list)

# Q3. Create a list and sort it. 
list1=[5,4,3,2,1]
list2=["Apple","Orange","Pineapple"]
list1.sort()
list2.sort()
print(list1)
print(list2)

# Q4. Create a list of numbers and print sum of all the elements. 
list=[1,2,3,4,5]
s=0
for i in list:
    s=s+i
print("Sum of all elements",s)

# Q5.Program to compare elements of list. 
def compare(lst):
    if lst[0] == lst[1]:
        print("All elements are the same.")
    else:
        print("The elements are not the same.")
compare([5, 5, 5, 5])
compare([1, 1, 3, 4])


# Q6. Program to find maximum and minimum of list. 
list1=[0,1,2,3,4,5,6,19,20]
list2=["Apple","Orange","Pineapple"]
print(min(list1))
print(max(list1))
print(min(list2))
print(max(list2))

# Q7. Count the occurrence of element in list. 
list=[1,2,2,2,3,4,5,1,1,1]
print(list.count(1))

# Q8. Reverse a list. 
list=[1,2,3,4,5]
list.reverse()
print(list)
         # OR
list=[1,2,3,4,5]
print(list[::-1])

# Q9. Write a loop that traverses the previous list and prints the length of each element. What 
# happens if you send an integer to len 
list=["apple","banana","orange","pineapple"]
for i in list:
    print(len(i))