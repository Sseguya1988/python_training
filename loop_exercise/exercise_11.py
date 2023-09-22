# Exercise 11: Write a program to display all prime numbers within a range
# lets begin by defining a function to check for a prime number
def is_prime(number):
    # A prime number is greater than one
    if number <= 1:
        return False
    # check for factors from 2 to the sqrt of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# input a range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
# validate this range
if start > end:
    print("Invalid range, start should be less or equal to end")
else:
    print(f"Prime numbers in the range {start} to {end}")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
