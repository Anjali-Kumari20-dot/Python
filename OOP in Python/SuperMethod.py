class Car:
    name = "anonymous"

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped.")

    def changeName(self, name):
        self.__class__.name = "Maruti"
        #self.__class__.Car

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type) 
        self.name = name
        super().start()

# car1 = ToyotaCar("Pirus", "Electric")
# print(car1.type)

car2 = Car()
car2.changeName("Maruti")
print(car2.name)
print(Car.name)