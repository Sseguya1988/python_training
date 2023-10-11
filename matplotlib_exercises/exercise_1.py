# Exercise 1: Read Total profit of all months and show it using a line plot
import pandas as pd
import matplotlib.pyplot as plt

# Load the csv file
sales_data = pd.read_csv("company_sales_data.csv")

# extract "Months" and "Total profit" data
months = sales_data["month_number"]
profits = sales_data["total_profit"]

# create a line plot
plt.plot(months, profits, marker="o", linestyle="-.", color="g", markersize="5")

# set the labels for X and Y axes
plt.xlabel("Months")
plt.ylabel("Total Profits")

# add a grid
plt.grid(True, linestyle="-", color="gray", linewidth="0.5")

# set title of the plot
plt.title("Total Profits over Months")

# show the plot
plt.show()
