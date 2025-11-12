# OOPS -> Object Oriented Programming

# 1. Encapsulation
# 2. Inheritence
# 3. polymorphism
# 4. Abstraction --> not natively available

# Inheritence --> 1. single Inheritence 2. multi-level Inheritence
# 3. multiple Inheritence 4. Hybrid Inheritence

# --> parent class (base class) 
# --> child class (inherited class/derived class)

# 1. single inheritense

class Car:  # parent class
    def start(self):
        print("Car Started")
    def stop(self):
        print("Car Stopped")

class ElectricCar(Car):  # child class
    def charge(self):
        print("Battery Chargning..")


# xev = ElectricCar()

# xev.charge()
# xev.start()
# xev.stop()


# 2. multi-level inheritense

class GrandFather:
    def house(self):
        print("GrandFather's House")
    
class Father(GrandFather):
    def guest_house(self):
        print("Father's guest house")

class Son(Father):
    def car(self):
        print("Son won's a car")

# child = Son()
# child.house()
# child.guest_house()
# child.car()
        
# 3. multiple inheritense

class Father():
    def knows_telugu(self):
        print("Father knows Telugu")

class Mother():
    def knows_kannada(self):
        print("Mother knows Kannada")
        
class Son(Father, Mother):
    def knows_english(self):
        print("Son knows English")
        
# child = Son()
# child.knows_english()
# child.knows_kannada()
# child.knows_telugu()  


# Hierarchical Inheritence
class Father():
    def guest_house(self):
        print("Father's guest house")

class FirstSon(Father):
    def car(self):
        print("First Son won's a car")
        
class SecondSon(Father):
    def bike(self):
        print("Second Son won's a bike") 


child2 = SecondSon()
child1 = FirstSon()


# Diamond Inheritence

class Father():
    def guest_house(self):
        print("Father's guest house")

class FirstSon(Father):
    def car(self):
        print("First Son won's a car")
        
class SecondSon(Father):
    def bike(self):
        print("Second Son won's a bike") 
        
class GrandDaughter(FirstSon, SecondSon):
    pass


child2 = SecondSon()
child1 = FirstSon()

daughter = GrandDaughter()
# daughter.



# polymorphism

class Car:
    def drive(self):
        print("Driving on road")
        
class Boat:
    def drive(self):
        print("Driving on water")

class Plane:
    def drive(self):
        print("Flying on sky")
        
car = Car()
boat = Boat()
plane = Plane()

# car.drive()
# boat.drive()
# plane.drive()


class Bird:
    def fly(self):
        print("Bird can fly")
        
class Parot(Bird):
    def fly(self):
        print("Parot can fly")

class Chicken(Bird):
    def fly(self):
        print("Though it has wings it can't fly")
        
class Pegion(Bird):
    pass


# parot = Parot()
# parot.fly()

# chick = Chicken()
# chick.fly()

# pegion = Pegion()
# pegion.fly()


def adds(a, b, c=0):
    return a + b + c

print(adds(1, 2, 5))
print(adds(1, 2))

# method overriding and method overloading