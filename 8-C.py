# Class to illustrate constructor

class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display details
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating an object
s1 = Student("Akhil", 20)

# Display student details
s1.display()