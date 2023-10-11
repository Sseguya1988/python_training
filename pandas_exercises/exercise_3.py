# Exercise 3: Find the most expensive car company name
import pandas as pd

# load the CSV file
car_data = pd.read_csv("Automobile_data.csv")

# Find row with maximum price
most_expensive_car = car_data[car_data["price"] == car_data["price"].max()]

# extract company name and price
company_name = most_expensive_car.iloc[0]["company"]
car_price = most_expensive_car.iloc[0]["price"]

# print the most expensive car company and the price
print(f"The most expensive car is from {company_name} and its price is ${car_price}")

"""
# load the CSV file
car_data = pd.read_csv("Automobile_data.csv")

# sort the data by price in descending order
car_data.sort_values(by="price", ascending=False, inplace=True)

# extract the most expensive car
most_expensive_car = car_data.iloc[0]

# extract the company name
company_name = most_expensive_car["company"]
car_price = most_expensive_car["price"]
print(f"The most expensive car is from {company_name} and its price is ${car_price}")
"""

