# nested python functions

# uses

# 1. Encapsulation --> hiding helper logic from external access
# 2. code organization --> grouping related functionality for cleaner code
# 3. Access to Outer Variables --> inner functions can use variables of the outer function.

def outer():
    print("I'm a outer function")
    def inner():
        print("Hey I'm a inner function")
    inner()

# outer()

# inner()

def greet(name: str):
    message = "Hey good morning"
    def display():
        # return f"{message} {name}"   -- 
        return "{0} {1}".format(message, name)
    return display()

res = greet(name="Dhoni")
print(res)
        
