# Exercise 9: Check Palindrome Number
def is_palindrome(num):
    num_string = str(num)
    # reverse this string
    reversed_string = num_string[::-1]
    return num_string == reversed_string


# Apply this function
test_number = int(input("Enter number under investigation: "))

# use a for loop to apply this function
if is_palindrome(test_number):
    print(f"{test_number} is a palindrome")
else:
    print(f"{test_number} is not a palindrome")

