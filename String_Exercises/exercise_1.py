# Exercise 1A: Create a string made of the first, middle and last character
def new_string(input_string):
    length = len(input_string)

    # check if the string is longer two characters
    if length < 3:
        return "Input string is too short"
    # calculate index of middle character
    middle_term = length // 2

    # construct a new string
    modified_string = input_string[0] + input_string[middle_term] + input_string[-1]
    return modified_string


# apply this function
input_string = input("Enter your sting: ")
result = new_string(input_string)
print(result)
