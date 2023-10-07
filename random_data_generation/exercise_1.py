# Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5
import random
# crate an empty list
random_list = []
# iterate over a range of three
for _ in range(3):
    num = random.randrange(100, 999, 5)
    random_list.append(num)
# print this random list
print(random_list)
