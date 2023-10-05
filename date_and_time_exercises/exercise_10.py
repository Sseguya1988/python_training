# Exercise 10: Calculate number of days between two given dates
from datetime import datetime
# First date
date_1 = datetime(2020, 2, 25)
# Second date
date_2 = datetime(2020, 9, 17)
# extract number of days between them
num_days = (date_2 - date_1).days
print(f"{num_days} days")

