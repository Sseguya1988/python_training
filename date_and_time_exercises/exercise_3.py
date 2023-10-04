# Exercise 3: Subtract a week (7 days)  from a given date in Python
from datetime import datetime, timedelta
# Given date
given_date = datetime(2020, 2, 25)
# subtract 7 days from this date
new_date = given_date - timedelta(days=7)
print(new_date)
