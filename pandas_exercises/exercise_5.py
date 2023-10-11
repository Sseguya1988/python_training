# Exercise 5: Count total cars per company
import pandas as pd

# Load CSV file
car_data = pd.read_csv("Automobile_data.csv")

# extract number of cars per company
car_numbers = car_data["company"].value_counts()

# print number of cars per company
print(car_numbers)
