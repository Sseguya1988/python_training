# Exercise 7: String characters balance Test
def balance_test(s1, s2):
    # convert strings to sets to eliminate repeated items
    set_s1 = set(s1)
    set_s2 = set(s2)
    # check if s1 is a subset of s2
    return set_s1.issubset(set_s2)


# apply this function
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
balanced = balance_test(s1, s2)
if balanced:
    print("True")
else:
    print("False")
