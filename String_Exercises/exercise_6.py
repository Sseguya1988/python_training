# Exercise 6: Create a mixed String using the following rules
def create_new_string(s1, s2):
    char_s1 = list(s1)
    char_s2 = list(s2)
    # initialize
    result = ""
    # use while function to create new string
    while char_s1 or char_s2:
        if char_s1:
            result += char_s1.pop(0)
        if char_s2:
            result += char_s2.pop(-1)
    return result


# use this function
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
new_result = create_new_string(s1, s2)
print(new_result)
