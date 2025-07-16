class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def interact(self):
        raise Exception("Error")

class Applicant(User):
    def interact(self):
        return self.apply_to_job()

    def apply_to_job(self):
        return f"{self.username} is applying to a job."

class Employer(User):
    def interact(self):
        return self.post_job()

    def post_job(self):
        return f"{self.username} is posting a job."


# Test
users = [
    Applicant("Ali", "ali@mail.com"),
    Employer("Bob", "bob@company.com")
]

for user in users:
    print(user.interact())