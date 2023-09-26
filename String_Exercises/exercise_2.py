# Exercise 1B: Create a string made of the middle three characters
def create_string(input_string):
    if len(input_string) < 5:
        return "Entered string is too short"
    # indicate the start index for the three middle items
    start_middle = len(input_string) // 2 - 1
    # extract the middle three items
    new_string = input_string[start_middle:start_middle + 3]
    return new_string


# apply this definition
input_string = input("Enter your string: ")
result = create_string(input_string)
print(result)
