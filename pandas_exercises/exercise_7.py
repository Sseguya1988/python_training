# Exercise 7: Find the average mileage of each car making company
import pandas as pd

# load csv file
car_data = pd.read_csv("Automobile_data.csv")

# extract average for each car making company
average_mileage = car_data.groupby("company")["average-mileage"].mean()

# print the companies with corresponding mileage
print(average_mileage)
