class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self):
        self.type = type

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Pirus")
car3 = Fortuner("diesel")

print(car3.name)
print(car3.start())
print(car3.color)
