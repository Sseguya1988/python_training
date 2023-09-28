# Exercise 9: Calculate the sum and average of the digits present in a string
def sum_and_average(input_string_s1):
    # initialize the digit sum and digit count
    digit_sum = 0
    digit_count = 0
    # iterate through each character of the string
    for char in input_string_s1:
        if char.isdigit():
            digit_sum += int(char)
            digit_count += 1  # increment for the count
    # calculate the average
    if digit_count > 0:
        digit_average = digit_sum / digit_count
    else:
        digit_average = 0  # this avoids disability by zero
    return digit_sum, digit_average


# apply this function
input_string_s1 = input("Enter your desired string: ")
sum_of_digits, average_of_digits = sum_and_average(input_string_s1)
print(f"The sum of digits in the string is {sum_of_digits} and the average is {average_of_digits}")

