# Exercise 14: Reverse a given integer number
def reverse_digits(number):
    # check if the number is negative
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    # covert number to string, reverse it and convert it back to number
    reversed_str = str(number)[::-1]
    reversed_number = int(reversed_str)
    # if the original number is negative, make reversed number is negative,
    if is_negative:
        reversed_number = - reversed_number
    return reversed_number


# input a number from user
num = int(input("Enter the number whose digits are to be reversed: "))
reverse_num = reverse_digits(num)
print(reverse_num)
