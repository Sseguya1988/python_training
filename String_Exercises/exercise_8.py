# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
import re

def count_usa_occurrences(input_string):
    pattern = re.compile(r"USA", re.IGNORECASE)
    # find all occurrences of USA
    occurrences = pattern.findall(input_string)
    return len(occurrences)


# Apply the definition
input_string = input("Enter a string: ")
usa_count = count_usa_occurrences(input_string)
print(f"The number of occurrences of 'USA' (case-insensitive) is: {usa_count}")
