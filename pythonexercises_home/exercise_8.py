# Exercise 8: Create an inner function
def out_function(str1, str2):
    def new_concat(string, str3):
        return string + str3

    concat_string = str1 + str2
    str3 = "Developers"
    result = new_concat(concat_string, str3)
    return result


# apply this function
string_one = input("Enter the first string: ")
string_two = input("Enter the second string: ")
final_result = out_function(string_one, string_two)
print(final_result)
