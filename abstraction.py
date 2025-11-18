# Abstraction

from abc import ABC, abstractmethod

# abstract class
class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        self.__check_system()
        print("Car Engine Started")
    
    def stop(self):
        print("Car Engine Stopped")
    
    def speed(self):
        print("Car can go 180 KMPH")
        
    def __check_system(self):
        print("Internal - Checking Oil, engine, and fuel system....")



# car.__check_system() # can I access it here ?

if __name__ == "__main__":
    print("Main Function Started")
    car = Car()
    car.start()
    car.stop()
    car.speed()
