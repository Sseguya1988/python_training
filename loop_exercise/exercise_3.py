# Exercise 3: Calculate the sum of all numbers from 1 to a given number
in_put = int(input("Enter a number: "))
# Use a for loop for to summ up numbers
sum_numbers = 0
for i in range(1, in_put+1):
    sum_numbers += i
print(f"The sum is: {sum_numbers}")

