# Exercise 18: Replace each special symbol with # in the following string
# Input string with special symbols
input_string = "Hello! This is a sample string with #special symbols."

# Define a set of special symbols to be replaced
special_symbols = "!@#$%^&*()_+-=[]{}|;':\",.<>?/\\"

# Initialize an empty result string
result_string = ""

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is a special symbol
    if char in special_symbols:
        # If it's a special symbol, add '#' to the result
        result_string += "#"
    else:
        # If it's not a special symbol, add the character unchanged
        result_string += char

# Print the result
print(result_string)
