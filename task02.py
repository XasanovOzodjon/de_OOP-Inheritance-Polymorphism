class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.km_counter = 0

    def start(self):
        return f"{self.name} is running."
    
    def stop(self):
        return f"{self.name} has stopped."
    
    @property
    def km(self):
        return self.km_counter
    

class Car(Vehicle):
    def __init__(self, name, model):
        super().__init__(name, model)

    def show_info(self):
        return f"Car Name: {self.name}, Model: {self.model}, KM: {self.km_counter}"
    
class Bike(Vehicle):
    def __init__(self, name, model):
        super().__init__(name, model)

    def show_info(self):
        return f"Bike Name: {self.name}, Model: {self.model}, KM: {self.km_counter}"
    
def main():
    car = Car(name="BMW", model="M3")
    bike = Bike(name="Yamaha", model="R3")

    print(car.start())
    print(car.show_info())
    print(car.stop())

    print(bike.start())
    print(bike.show_info())
    print(bike.stop())
    
if __name__ == "__main__":
    main()  