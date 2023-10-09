# Exercise 9: Roll dice in such a way that every time you get the same number
import random


# seed for random number generator
def roll_biased_die(seed):
    random.seed(seed)

    # list of possible outcomes with a bias
    out_comes = [1, 2, 3, 4, 5, 6]

    # simulate rolling a die using .choice()
    result = random.choice(out_comes)

    return result


# simulate rolling the dice 5 times with  the same seed
seed = 42
for _ in range(5):
    result = roll_biased_die(seed)
    print(f"The dice gives a result of {result}")
