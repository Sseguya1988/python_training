# Exercise 15: Remove special symbols / punctuation from a string
import re

input_string = input("Enter sting with special symbols and punctuations: ")
cleaned_string = re.sub(r"[^\w\s]", "", input_string)
print(cleaned_string)
