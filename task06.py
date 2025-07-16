class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def calculate_bonus(self):
        raise Exception("Bu metod bu uchun hali chaqirilmagan.")
    
class Developer(Employee):
    def __init__(self, name, position, p_language):
        super().__init__(name, position)
        self.programming_language = p_language

    def calculate_bonus(self):
        return f"{self.name} has a bonus of 10% for being a {self.position}."

class Manager(Employee):
    def __init__(self, name, position, team_size):
        super().__init__(name, position)
        self.team_size = team_size

    def calculate_bonus(self):
        return f"{self.name} has a bonus of 15% for managing a team of {self.team_size} members."
    
    
def main():
    dev = Developer(name="Ozod", position="Python Developer", p_language="Python")
    mgr = Manager(name="Ali", position="Project Manager", team_size=5)

    print(dev.calculate_bonus())
    print(mgr.calculate_bonus())

if __name__ == "__main__":
    main()