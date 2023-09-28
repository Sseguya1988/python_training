# Exercise 10: Write a program to count occurrences of all characters within a string
def count_characters(input_string):
    # create an empty dictionary
    character_counts = {}
    # iterate through each character in the string
    for char in input_string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts


# apply this definition
input_string = input("Enter the string: ")
result = count_characters(input_string)
print(result)
