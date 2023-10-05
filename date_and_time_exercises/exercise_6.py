# Exercise 6: Add a week (7 days) and 12 hours to a given date
from datetime import datetime, timedelta
# date given
given_date = datetime(2020, 3, 22, 10, 0, 0)
# adding 7 days and 12 hours
new_date = given_date + timedelta(days=7, hours=12)
print(new_date)
