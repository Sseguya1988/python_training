# Exercise 5: Read face cream and facewash product sales data and show it using the bar chart
import pandas as pd
import matplotlib.pyplot as plt


# Load the CSV data file
sales_data = pd.read_csv("company_sales_data.csv")

# extract "Month", "Face cream" and "Face wash" data from source csv file
months = sales_data["month_number"]
face_cream = sales_data["facecream"]
face_wash = sales_data["facewash"]

# define bar width
bar_width = 0.4

# generate a bar graph plot
plt.bar(months - bar_width/2, face_cream, bar_width, color="blue", label="Face cream Sales data")
plt.bar(months + bar_width/2, face_wash, bar_width, color="orange", label="Face wash Sales data")

# set the X and Y label
plt.xlabel("Sales units in number")
plt.ylabel("Month Number")

# set title for the graph
plt.title("Facewash and Facecream sales data")

# set the legend
plt.legend(loc="upper left")

# set the grid on
plt.grid(True, linestyle="dashed", color="grey", linewidth="0.5")

# show plot
plt.show()
