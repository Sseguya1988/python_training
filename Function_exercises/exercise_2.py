# Exercise 2: Create a function with variable length of arguments
def func1(*args):
    print("Printing values")
    for arg in args:
        print(f"Value: {arg}")


# Use the function
func1(1, 2, 3)
func1("Ivan", "Dogs", "Cats")
