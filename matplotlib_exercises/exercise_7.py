# Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges
import pandas as pd
import matplotlib.pyplot as plt

# load the CSV file for data source
sale_data = pd.read_csv("company_sales_data.csv")

# extract "Total profits" data to plot
total_profits = sale_data["total_profit"]

# define number of bins for the histogram
num_bins = 10

# generate histogram for this data
plt.hist(total_profits, bins=num_bins, color="b", label="Profit data")

# set the X and Y axis labels
plt.xlabel("profit range in dollar")
plt.ylabel("Actual profit in dollar")

# set the title
plt.title("Profit data")

# set the legend on
plt.legend(loc="upper left")

# show plot
plt.show()
