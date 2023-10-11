# Exercise 4: Print All Toyota Cars details
import pandas as pd

# Load the csv file
car_data = pd.read_csv("Automobile_data.csv")

# extract details of all toyota cars
toyota_details = car_data[car_data["company"] == "toyota"]

# print details of toyota cars
print(toyota_details)
