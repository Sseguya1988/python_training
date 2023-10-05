# Exercise 9: Calculate the date 4 months from the current date
from datetime import datetime, timedelta
# given date
given_date = datetime(2020, 2, 25).date()
# compute date four months after this
new_date = given_date + timedelta(days=4*30)
print(f"The current date is {given_date}")
print(f"The new date is {new_date}")


