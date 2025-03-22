# 1. Create a tuple and sort it. 
tup=(9,3,4,6,6,7,8,5)
print((sorted(tup)))

# 2. Create a tuple of numbers and print sum of all the elements. 
tup=(9,3,4,6,6,7,8,5)
s=0
for i in tup:
    s=s+i
print("Sum of all elements is",s)

# 3. Program to find maximum and minimum of tuple.
tup=(9,3,4,6,6,7,8,5)
print(max(tup))
print(min(tup))

# 4. Count the occurrence of element in tuple in a specific range.
tup=(9,3,4,6,6,7,8,5)
print(tup.count(6))

# 5. Reverse a tuple.
tup=(9,3,4,6,6,7,8,5)
print(tup[::-1])

# 6. Write a loop that traverses the previous tuple and prints the 
# length of each element. What happens if you send an floating 
# number in index?
tup=("apple","banana","orange","pineapple")
for i in tup:
    print(len(i))