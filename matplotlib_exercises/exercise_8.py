# Exercise 8: Calculate total sale data for last year for each product and show it using a Pie chart
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file for data source
sales_data = pd.read_csv("company_sales_data.csv")

# compute the annual totals for each item
annual_totals = sales_data.iloc[0:, 1:-2].sum(axis=0)
# print(annual_totals)

# generate a pie chart
plt.figure(figsize=(8, 8))
plt.pie(annual_totals, labels=annual_totals.index, autopct="%1.1f%%", startangle=140)

# set title
plt.title("Sales data")
plt.axis("equal")

# add a legend
plt.legend(annual_totals.index, title="Products", loc="lower right")

# show pie chart
plt.show()

"""
# grand annual total
grand_total = annual_totals.sum()

# add grand total to annual total series
annual_totals["Grand Total"] = grand_total

# generate a pie chart
plt.figure(figsize=(8, 8))
plt.pie(annual_totals, labels=annual_totals.index, autopct="%1.1f%%", startangle=140)

# set title
plt.title("Sales data")
plt.axis("equal")

# show pie chart
plt.show()

"""
