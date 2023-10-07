# Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
import random
# set an initial list of lottery tickets
lottery_tickets = []
for i in range(100):
    lottery_tickets.append(random.randint(1000000000, 9999999999))
print(lottery_tickets)
# sampled list
sampled_list = random.sample(lottery_tickets, 2)
print("The winning lottery ticket numbers are as follows:")
print(f"The winners are: {sampled_list}")
