class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def turn_on(self):
        return f"{self.brand} appliance is now ON."

    def turn_off(self):
        return f"{self.brand} appliance is now OFF."

class TV(Appliance):
    def __init__(self, brand, power, screen_size):
        super().__init__(brand, power)
        self.screen_size = screen_size

    def display_info(self):
        return f"TV Brand: {self.brand}, Power: {self.power}W, Screen Size: {self.screen_size} inches"
    
class Fridge(Appliance):
    def __init__(self, brand, power, capacity):
        super().__init__(brand, power)
        self.capacity = capacity

    def display_info(self):
        return f"Fridge Brand: {self.brand}, Power: {self.power}W, Capacity: {self.capacity} liters"
    
    
def main():
    tv = TV(brand="Samsung", power=150, screen_size=55)
    fridge = Fridge(brand="LG", power=200, capacity=300)

    print(tv.turn_on())
    print(tv.display_info())
    print(tv.turn_off())

    print(fridge.turn_on())
    print(fridge.display_info())
    print(fridge.turn_off())

if __name__ == "__main__":
    main() 