# Exercise 2: Convert string into a datetime object
from datetime import datetime
date_string = "Feb 25 2020 4:20PM"
# specify the format of date string
date_format = "%b %d %Y %I:%M%p"
# convert to datetime object
datetime_object = datetime.strptime(date_string, date_format)
print(datetime_object)
