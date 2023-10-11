# Exercise 10: Merge two data frames using the following condition
import pandas as pd

# state the given data frames in form of dictionaries
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}

# create pandas dataframes from dictionaries
data1 = pd.DataFrame(Car_Price)
data2 = pd.DataFrame(car_Horsepower)

# concatenate to form new dataframe
new_data = data1.merge(data2, on="Company")

print(new_data)
