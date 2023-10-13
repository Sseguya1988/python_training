# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

# input an integer to work with
num = int(input("Enter the integer to extract digits from: "))
# # xpress this digit as a string
num_str = str(num)
# reverse this string
num_str_reversed = num_str[::-1]
# split digit into integers
print(*num_str_reversed, sep=" ")
