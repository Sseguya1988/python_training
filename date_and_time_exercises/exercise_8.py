# Exercise 8: Convert the following datetime into a string
from datetime import datetime
# given datetime
given_date = datetime(2020, 2, 25)
# change format
format_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(format_date)
