# python class

# class --> functions (contructor function, regular functions), 
# data members (global and vars)

# syntax

# class ClassName:
#     def __init__(self, name, age, exp):
#         self.name = name
#         self.age = age
#         self.exp = exp

# class GreetMessage:
#     def display(self):
#         return "Good Morning!" 

# obj1 = GreetMessage()
# print(obj1.display())

class GreetMessage:
    def __init__(self, name: str):
        self.name = name
    
    def display(self):
        return f"Good Morning {self.name}" 

# obj2 = GreetMessage("Rohith")
# print(obj2.display())

# obj3 = GreetMessage("Karthik")
# print(obj3.display())


class Student:
    global default_name 
    default_name = "unknown name"
    def __init__(self, name: str, course:str, exp:int):
        print("Hey Student Class have been intiated")
        self.stu_name = name
        self.course = course
        self.stu_exp = exp
        
    def display_info(self):
        test_var = "null" # only restricted to this function
        return f"Name: {self.stu_name}, Course: {self.course}, Experience: {self.stu_exp}, test: {test_var}"
    
    def test(self):
        return default_name

RohithClsObject = Student("Rohith", "AzureDE", 2)
# LikithClsObject = Student("Likith", "AwsDE", 4)
# print(default_name)

print(RohithClsObject.display_info())
# print(LikithClsObject.display_info())

print(RohithClsObject.test())



    