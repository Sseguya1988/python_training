# Exercise 3: Remove items from a list while iterating
lst = list(range(10,100,10))
new_lst = []
for i in lst:
    if i <= 50:
        new_lst.append(i)
print(new_lst)







