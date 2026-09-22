from user import User

class Mentor(User):
    def display_details(self):
        super().display_details()
        print("Role : Mentor")