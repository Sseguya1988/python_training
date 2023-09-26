# Exercise 4: Arrange string characters such that lowercase letters should come first
def rearrange_string(input_string):
    lower_char = "".join(char for char in input_string if char.islower())
    upper_char = "".join(char for char in input_string if char.isupper())

    # form a new string
    new_string = lower_char + upper_char
    return new_string


# apply the definition
input_string = input("Enter your preferred string: ")
result = rearrange_string(input_string)
print(result)
