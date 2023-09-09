# Exercise 5: Display all duplicate items from a list
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
# Create empty lists for unique and duplicate numbers
uniq = []
dupl = []
# use for loop to determine the duplicate values
for i in sample_list:
    if i not in uniq:
        uniq.append(i)
    else:
        dupl.append(i)
# Print duplicate values in a list
print(dupl)

