# Exercise 5: Generate random String of length 5
import random
import string


# form a definition to generate a string of length 5
def random_string(length):
    # should include both upper and lowercase characters
    result_rand_str = "".join(random.choice(string.ascii_letters) for i in range(length))
    # print this random list
    print(result_rand_str)


# apply this function
random_string(5)
