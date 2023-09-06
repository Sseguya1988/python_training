# Exercise 1: Reverse each word of a string

words = input("Enter a sentence: ").split()
reverse_words = []
for i in words:
    reverse_words.append(i[::-1])
new_sentence = " ".join(reverse_words)
print(new_sentence)

