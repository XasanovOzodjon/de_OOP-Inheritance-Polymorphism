class User:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    
    def get_info(self):
        return f"Name: {self.name}, ID: {self.ID}"

    def get_dashboard(self):
        return "General dashboard"

class Student(User):
    def __init__(self, name, ID, courses):
        super().__init__(name, ID)
        self.courses = courses

    def get_dashboard(self):
        return self.courses

class Instructor(User):
    def __init__(self, name, ID, expertise):
        super().__init__(name, ID)
        self.expertise = expertise
        
    def get_dashboard(self):
        return {
            "students_count": 120,
            "courses_created": 5,
            "expertise": self.expertise
        }
def main():
    student = Student(name="Ozodjon Xasanov", ID="S123", courses=["Math", "Science"])
    instructor = Instructor(name="Ali Boboyev", ID="I456", expertise="Physics")

    print(student.get_info())
    print("Student Dashboard:", student.get_dashboard())

    print(instructor.get_info())
    print("Instructor Dashboard:", instructor.get_dashboard())     
        

