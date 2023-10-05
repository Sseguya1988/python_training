# Exercise 4: Print a date in a the following format, Day_name  Day_number  Month_name  Year
from datetime import datetime
given_date = datetime(2020, 2, 25)
# express in required format
new_date_format = given_date.strftime("%A %d %B %Y")
print(new_date_format)
