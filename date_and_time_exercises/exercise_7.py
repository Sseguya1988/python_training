# Exercise 7: Print current time in milliseconds
import time
# Get current time in seconds
current_time = time.time()
# convert time to milliseconds
new_current_time = int(current_time*1000)
print(new_current_time)

