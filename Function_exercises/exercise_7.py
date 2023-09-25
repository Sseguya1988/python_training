# Exercise 7: Assign a different name to function and call it through the new name
def display_student(name, age):
    print(f"Student's name: {name}")
    print(f"Student's age: {age}")


# re-assign the function
show_student = display_student
# use the new function
show_student("Alice", 35)

