# python class extension

class MyClassParent():  # parent class
    def __init__(self):
        self.message = "Good Morning"
        self.__name = "Virat"  # private variable
        
    def __construct_message(self): # private function or method
        return f"{self.message} {self.__name}"
    
    def display(self):
        return self.__construct_message()

    def construct_array(self, *args):
        return list(args)
    
    def construct_dict(self, **kwargs):
        return kwargs
    
# obj1 = MyClass()
# print(obj1.display())
# print(obj1.construct_array(1, 2, 3, 4 ,5, 6, 7))
# print(obj1.construct_array(1, 2, 3, 4 ,5, 6, 7, 8, 9, 10))
# print(obj1.construct_array(1, 2, 3))

# print(obj1.construct_dict(name="sandeep", age=29, course="MSc"))

# methods --> kwargs args


