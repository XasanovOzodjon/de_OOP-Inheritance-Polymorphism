class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        raise Exception("Error")
    

class EmailNotification(Notification):
    def __init__(self, message, email):
        super().__init__(message)
        self.email = email

    def send(self):
        return f"Email: {self.email}, Message: {self.message}"
    

class SMSNotification(Notification):
    def __init__(self, message, phone_number):
        super().__init__(message)
        self.phone_number = phone_number

    def send(self):
        return f"SMS to {self.phone_number}: {self.message}"
    
def main():
    email_notification = EmailNotification(message="Salom Dunyo bu emailga", email="Ozod@example.com")
    sms_notification = SMSNotification(message="Hello, this is a SMS!", phone_number="+998958281166")

    print(email_notification.send())
    print(sms_notification.send())

if __name__ == "__main__":
    main()