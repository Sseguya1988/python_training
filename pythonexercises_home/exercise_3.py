# Exercise 3: Remove items from a list while iterating
lst = list(range(10,100,10))
# Create an empty list
new_lst = []
# Use a for loop
for i in lst:
    if i <= 50:
        new_lst.append(i)
print(new_lst)







