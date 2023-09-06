# Remove values greater than 50 from a list

number_list = list(range(10,100,10))
print(number_list)
number_list1 = []
for i in number_list:
    if i % 10 == 0:
        number_list1.append(i)
    else:



