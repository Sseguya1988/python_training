# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# define a function to compute exponents of a number
def exponent(base, exp):
    num_base = int(base)
    num_exp = int(exp)
    result = num_base**num_exp
    return result


# Apply this function
base_num = input("Enter the base number: ")
exp = input("Enter the exponent number: ")

final_result = exponent(base_num, exp)
print(f"base = {base_num} \nexponent = {exp}")
print(f"{base_num} raised to the power {exp}: {final_result}")
