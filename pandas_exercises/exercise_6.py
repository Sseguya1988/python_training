# Exercise 6: Find each company’s Highest price car
import pandas as dp
import pandas as pd

# Load csv file
car_data = pd.read_csv("Automobile_data.csv")

# group the data by company and find the highest price for each group
max_price_indices = car_data.groupby("company")["price"].idxmax()

# extract rows corresponding to high prices
highest_price = car_data.loc[max_price_indices, ["company", "company", "price"]]

# print companies with their highest priced cars
print(highest_price.to_string(index=False))

