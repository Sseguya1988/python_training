# Exercise 2: Clean the dataset and update the CSV file
import pandas as pd

# load the csv data file
car_data = pd.read_csv("Automobile_data.csv")

# replace ?, n.a or NaN with pd.NA
car_data.replace(["?", "n.a", "NaN"], pd.NA, inplace=True)

# save cleaned file back to a csv
car_data.to_csv("Cleaned dataset.csv", index=False)
