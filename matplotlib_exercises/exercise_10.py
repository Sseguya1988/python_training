# Exercise Question 10: Read all product sales data and show it using the stack plot
import pandas as pd
import matplotlib.pyplot as plt

# load the CSV file as data source
sales_data = pd.read_csv("company_sales_data.csv")

# extract data for each product
months = sales_data["month_number"]
products = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]
colors = ["magenta", "cyan", "red", "black", "green", "yellow"]

# form an empty list
product_data = []

for product in products:
    product_data.append(sales_data[product])

# generate a stack plot for product sales
plt.stackplot(months, product_data, labels=products, colors=colors, alpha=1)

# set X, Y axis labels and title
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.title("All product sales data using stack plot")

# add legend
plt.legend(loc="upper right")

# show plot
plt.show()


