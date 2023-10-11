# Exercise 3: Read all product sales data and show it  using a multiline plot
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file data source
sales_data = pd.read_csv("company_sales_data.csv")

# extract "Months", "Face cream", "Face wash", "Tooth paste", "Bathing soap", "Shampoo" and "Moisturizer" data
months = sales_data["month_number"]
face_cream = sales_data["facecream"]
face_wash = sales_data["facewash"]
tooth_paste = sales_data["toothpaste"]
bathing_soap = sales_data["bathingsoap"]
shampoo = sales_data["shampoo"]
moisturizer = sales_data["moisturizer"]

# generate plots for sales units over months
plt.plot(months, face_cream, marker="o", color="b", linestyle="-", linewidth="3", markersize="6", label="Face cream Sales Data")
plt.plot(months, face_wash, marker="o", color="orange", linestyle="-", linewidth="3", markersize="6", label="Face wash Sales Data")
plt.plot(months, tooth_paste, marker="o", color="g", linestyle="-", markersize="6", linewidth="3", label="Tooth Paste Sales Data")
plt.plot(months, bathing_soap, marker="o", color="r", linestyle="-", markersize="6", linewidth="3", label="Bathing Soap Sales Data")
plt.plot(months, shampoo, marker="o", color="m", linestyle="-", markersize="6", linewidth="3", label="Shampoo Sales Data")
plt.plot(months, moisturizer, marker="o", color="#8B4513", linestyle="-", markersize="6", linewidth="3", label="Moisturizer Sales Data")

# set X and Y labels
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")

# set title
plt.title("Sales data")

# add a legend
plt.legend(loc="upper left")

# show plot
plt.show()
