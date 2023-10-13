# Exercise 9: Read Bathing soap facewash of all months and display it using the Subplot
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file as a data source
sales_data = pd.read_csv("company_sales_data.csv")

# extract items to plot
plot_items = ["bathingsoap", "facewash"]
colors = ["black", "red"]

# create a figure with two subplots
fig, axes = plt.subplots(len(plot_items), 1, figsize=(6, 10), sharex=True)

# generate the plots
for i, (item, color) in enumerate(zip(plot_items, colors)):
    axes[i].plot(sales_data["month_number"], sales_data[item], marker="o", linestyle="-", color=color)
    axes[i].set_ylabel("Sales units in number")
    axes[i].set_title(f"Sales data of a {item}")

# set common xlabel
plt.xlabel("Months Number")

# Adjust layout and show plots
plt.tight_layout()
plt.show()
