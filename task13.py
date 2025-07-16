class Courier:
    def __init__(self, name):
        self.name = name

    def delivery_range(self):
        raise Exception("This method should be overridden by subclasses")

class BikeCourier(Courier):
    def __init__(self, name, bike_type):
        super().__init__(name)
        self.bike_type = bike_type

    def delivery_range(self):
        return "Delivers within the city limits"


class CarCourier(Courier):
    def __init__(self, name, car_model):
        super().__init__(name)
        self.car_model = car_model

    def delivery_range(self):
        return "Delivers within the city and nearby areas"
    
class DroneCourier(Courier):
    def __init__(self, name, drone_model):
        super().__init__(name)
        self.drone_model = drone_model

    def delivery_range(self):
        return "Delivers within the city and can reach remote areas"
    
def main():
    bike_courier = BikeCourier(name="John", bike_type="Mountain Bike")
    car_courier = CarCourier(name="Alice", car_model="Toyota Prius")
    drone_courier = DroneCourier(name="Bob", drone_model="DJI Phantom")

    print(f"{bike_courier.name} ({bike_courier.bike_type}): {bike_courier.delivery_range()}")
    print(f"{car_courier.name} ({car_courier.car_model}): {car_courier.delivery_range()}")
    print(f"{drone_courier.name} ({drone_courier.drone_model}): {drone_courier.delivery_range()}")
