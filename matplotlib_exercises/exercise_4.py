# Exercise 4: Read toothpaste sales data of each month and show it using a scatter plot
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data file
sales_data = pd.read_csv("company_sales_data.csv")

# extract the "Month" and "Toothpaste" data
months = sales_data["month_number"]
tooth_paste = sales_data["toothpaste"]

# generate a scatter plot
plt.scatter(months, tooth_paste, color="b", marksize="6", label="Tooth paste Sales data")

# set X and Y axis label
plt.xlabel("Month Number")
plt.ylabel("Number of units Sold")

# set title
plt.title("Tooth paste Sales data")


# set legend
plt.legend(loc="upper left")

# set the
