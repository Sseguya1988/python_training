# The list of numbers to be checked
numbers_x = [5, 2, 3, 4, 5]
numbers_y = [12, 2, 3, 4, 10, 11, 12]
# command to check if the first and last number in the string is the same
if numbers_y[0] == numbers_y[-1]:
    print(f"Given list: {numbers_y}", "result is True", sep="\n")
else:
    print(f"Given list: {numbers_y}", "result is False", sep="\n")
