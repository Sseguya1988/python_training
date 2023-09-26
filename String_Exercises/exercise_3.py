# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
def create_new_string(s1, s2):
    middel_index_1 = len(s1) // 2
    middle_index_2 = len(s2) // 2

    # create new string with first, middle and last items
    s3 = s1[0] + s2[0] + s1[middel_index_1] + s2[middle_index_2] + s1[-1] + s2[-1]
    return s3


# apply this function
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
result = create_new_string(s1, s2)
print(result)
