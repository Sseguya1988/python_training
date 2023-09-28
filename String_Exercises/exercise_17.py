# Exercise 17: Find words with both alphabets and numbers
import re

input_string = input("Enter a string: ")
# use regular expression re module to find words eith both alphabets and numbers
pattern = r"\w*\d\w*"
matching_words = re.findall(pattern, input_string)
print("Words with both alphabets and numbers: ")
for words in matching_words:
    print(words)
