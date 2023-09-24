# Exercise 4: Create a function with a default argument
def show_employee(name, salary=9000):
    print(f"Name: {name} salary: {salary}")


# use this function
# name = input("Enter name of the employee: ")
# salary = input("Enter the salary of the employee: ")
show_employee("Mark")
show_employee("Jude", 12000)
