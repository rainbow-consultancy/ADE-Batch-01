# super keyword

class Parent:
    def __init__(self):
        print("Parent constructer called")
    
    def house(self):
        print("Fathers House")

class Child(Parent):
    def __init__(self):
        super().__init__()  # calls parent construtor method
        print("Child constructer called")
        
    def house(self):
        super().house()
        print("Childs House")


# obj = Child()
# obj.house()


class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person Name is {self.name}")


class Student(Person):
    def __init__(self, name, roll_num):
        super().__init__(name)
        # self.name = name
        self.roll_num = roll_num
        print(f"student roll number {self.roll_num}")


student = Student("Sandeep", 501)
