# Exercise 18: Print the following pattern
num_rows = 5
# print upper part of the triangle
for i in range(num_rows):
    for j in range(i+1):
        print("*", end=" ")
    print()
# print lower pattern
for i in range(num_rows-1,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
