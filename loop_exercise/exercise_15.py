# Exercise 15: Use a loop to display elements from a given list present at odd index positions
def odd_position_elements(lst):
    for i in range(len(lst)):
        if i % 2 == 0:  # consider only odd number indexed items
            print(lst[i])


# input a list from a user
input_list = input("Enter a list of elements separated by spaces: ").split()
print("Elements at odd positions")
odd_position_elements(input_list)
