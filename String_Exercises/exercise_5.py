# Exercise 5: Count all letters, digits, and special symbols from a given string
def count_string_items(input_string):
    # initialize counters
    letter_count = 0
    digit_count = 0
    symbol_count = 0

    # set up a counter
    for char in input_string:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    return letter_count, digit_count, symbol_count


# use this function
input_string = input("Enter a string with letters, digits and any other symbols: ")
letters, digits, symbols = count_string_items(input_string)

# Print the counts
print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Symbols: {symbols}")
