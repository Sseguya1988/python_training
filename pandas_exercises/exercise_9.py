# Exercise 9: Concatenate two data frames using the following conditions
import pandas as pd

# state the two dictionaries
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500, 58900]}

# create dataframes from dictionaries
data1 = pd.DataFrame(GermanCars)
data2 = pd.DataFrame(japaneseCars)

# concatenate to a single dataframe
new_data_frame = pd.concat([data1, data2], keys=["Germany", "Japan"])

# print new_data_frame
print(new_data_frame)
