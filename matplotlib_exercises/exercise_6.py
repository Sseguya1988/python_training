# Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file for data source
sales_data = pd.read_csv("company_sales_data.csv")

# extract "Months" and "Bathing soap" data for plotting
months = sales_data["month_number"]
bathing_soap = sales_data["bathingsoap"]

# generate a plot for this
plt.bar(months, bathing_soap, color="b")

# set X and Y axis labels
plt.xlabel("Months Number")
plt.ylabel("Sales units in number")

# set the title
plt.title("bathingsoap sales data")

# set the grid on
plt.grid(True, color="grey", linewidth="0.5", linestyle="dashed")

# show plot
plt.show()
