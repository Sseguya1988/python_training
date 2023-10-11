# Exercise 8: Sort all cars by Price column
import pandas as pd
# import random

# load csv file
car_data = pd.read_csv("Automobile_data.csv")

# Group data by price
grouped_car_data = car_data.groupby("company")

# sort car data by price
# sorted_car_data = grouped_car_data.apply(lambda x: x.sample(frac=1, random_state=random.seed()))
sorted_car_data = grouped_car_data.apply(lambda x: x.sort_values(by="price"))

# reset index upon sorting
sorted_car_data.reset_index(drop=True, inplace=True)
# print new grouped car data
print(sorted_car_data.to_string(index=False))
