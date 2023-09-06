# Exercise 3: Print characters from a string that are present at an even index number

# Input string
word = input("Input a string: ")
for x in range(len(word)):
    if x % 2 == 0:
        print(word[x], end="\n")
    # Alternatively
# print("Even characters: ", word[::2])


