# Ask user form their name
name = input("What's your name? ").strip().title()
# ask the name of their friend
friend = input("What's the name of your best friend? ")
# Reply your feeling aboutn new user
"""
Anything here is commented
"""
# print("Happy to meet you,",name)
# above line can also be coded as follows
print("Happy to meet you, " + name, "and " + friend)
"""
In case you are encountered with a problem of dealing with two prints,
print("Happy to meet you ", end="", sep="") sep for separation between parameters
print(name) 
\" helps to print the character " (it's called escaping)
"""
# line 11 above can be presented as
"""
# Remove white space from str
name = name.strip()

# Capitalize users name, title capitalizes each first character in the word
# name = name.capitalize()
name = name.title()
"""
print(f"Happy to meet you, {name} and {friend}")
