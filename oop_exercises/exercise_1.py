# Exercise 1: Create a Class with instance attributes
class students:
    def __init__(self, marks, grade):
        self.marks = marks
        self.grade = grade


# create instances for marks
student1 = students(56, "C-")
student2 = students(72, "B+")
# access and print attributes of the instances
print(f"Student1 marks obtained: {student1.marks} and the grade is {student1.grade}")
print(f"Student2 marks obtained: {student2.marks} and the grade is {student2.grade}")
