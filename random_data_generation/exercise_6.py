# Exercise 6: Generate a random Password which meets the following conditions:
# - Password length must be 10 characters long.
# - It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
import random
import string


def random_password():
    # Ensure at least two uppercase letters
    uppercase_letters = [random.choice(string.ascii_uppercase) for _ in range(2)]

    # set at least one digit
    digit = random.choice(string.digits)

    # ensure at least one punctuation symbol
    punctuation_symbol = random.choice(string.punctuation)

    # Generate other characters
    random_source = string.ascii_uppercase + string.digits + string.punctuation
    other_characters = [random.choice(random_source) for _ in range(6)]

    # combine parts and reshuffle
    combined_password = uppercase_letters + [digit, punctuation_symbol] + other_characters
    random.SystemRandom().shuffle(combined_password)
    password = "".join(combined_password)

    return password


# apply this definition
print(f"The generated password is {random_password()}")


"""
import random
import string


def random_password():
    random_source = string.ascii_uppercase + string.digits + string.punctuation
    # select one upper case
    password = random.choice(string.ascii_uppercase)
    # select one digit
    password += random.choice(string.digits)
    # select one special symbol
    password += random.choice(string.punctuation)

    # generate other characters
    for i in range(7):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = "".join(password_list)
    return password


# Print a random password
print(f"The generated random password is : {random_password()}")
"""

