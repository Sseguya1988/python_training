# Exercise 5: Find the day of the week of a given date
from datetime import datetime
given_date = datetime(2020, 7, 26)
# extract the day of the week
week_day = given_date.strftime("%A")
print(week_day)
