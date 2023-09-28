# Exercise 16: Removal all characters from a string except integers
import re

# Input a string with mixed characters
input_string = input("Enter a string with mixed characters: ")
# Use regular expression to remove all non-digit characters
cleaned_string = re.sub(r"[^0-9]", "", input_string)
# Print the cleaned string containing only integers
print(cleaned_string)
