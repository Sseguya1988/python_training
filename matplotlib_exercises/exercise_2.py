# Exercise 2: Get total profit of all months and show line plot with the following Style properties
import pandas as pd
import matplotlib.pyplot as plt

# Load the csv data file
sales_data = pd.read_csv("company_sales_data.csv")

# extract "Months" and "Total Profits" data
months = sales_data["month_number"]
profits = sales_data["total_profit"]

# generate plot for the total profits over months
plt.plot(months, profits, marker="o", linestyle="dashed", color="r", linewidth="3", markerfacecolor="k", markersize="6", label="Total Profits")

# set X and Y labels
plt.xlabel("Month Number")
plt.ylabel("Solid units number")

# add a legend
plt.legend(loc="lower right")

# plot this graph
plt.show()
