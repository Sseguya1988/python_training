# Exercise 7: Calculate multiplication of two random float numbers
import random
# define the first float number
random_num1 = float(round(random.random(), 1))
random_num2 = float(round(random.uniform(95, 99.5), 1))
product_of_rand = random_num1 * random_num2
print(f"The first random number is {random_num1} is multiplied with the second random number {random_num2} to give a product of {product_of_rand}")
