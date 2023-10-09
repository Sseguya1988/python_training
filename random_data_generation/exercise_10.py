# Exercise 10: Generate a random date between given start and end dates
import random
from datetime import datetime, timedelta

# start and end dates
start_date = datetime(2023, 1, 2)
end_date = datetime(2023, 10, 9)
# range of dates
date_range = end_date - start_date
# generate random number of days within date range
random_days = random.randint(0, date_range.days)
random_date = start_date + timedelta(days=random_days)
print(f"The random date is", random_date.strftime("%Y-%m-%d"))
