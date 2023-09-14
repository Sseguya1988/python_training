# Exercise 4: Display float number with 2 decimal places using print()
float_num = 3.4527354
decimal_2 = "{:.2f}".format(float_num)
print(decimal_2)
"""
# Alternative 1
float_num = 1.234562
print(round(float_num, 2))
"""
"""
# Alternative 2
float_num = 1.2573645
# reduce float decimal numbers to 2 (.2f)
decimal_2 = f"{float_num:.2f}"
print(decimal_2)
"""


