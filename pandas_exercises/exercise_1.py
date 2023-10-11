# Exercise 1: From the given dataset print the first and last five rows
import pandas as pd

# create a pandas Data Frame from a csv file
file_path = "Automobile_data.csv"
cars_dtframe = pd.read_csv(file_path)
print("Python Pandas printing first 5 rows")
# print the first five rows
print(cars_dtframe.head())
print("Python Pandas printing last 5 rows")
# print the last five rows
print(cars_dtframe.tail())
"""
# Python dict object
student_dict = {'Name': ['Joe', 'Nat'], 'Age': [20, 21], 'Marks': [85.10, 77.80]}
print(student_dict)

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)
"""
