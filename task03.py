class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        return f"User: {self.username}, Email: {self.email}"


class Admin(User):
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)
        self.admin_level = admin_level

    @override
    def display_info(self):
        return f"Admin: {self.username}, Email: {self.email}, Level: {self.admin_level}"
    
    
class Guest(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    @override
    def display_info(self):
        return f"Guest: {self.username}, Email: {self.email}"
    
def main():
    admin = Admin(username="admin_user", email="admin@example.com", admin_level=1)
    guest = Guest(username="guest_user", email="guest@example.com")

    print(admin.display_info())
    print(guest.display_info())

if __name__ == "__main__":
    main()