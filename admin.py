from user import User

class Admin(User):
    def display_details(self):
        return super().display_details()
    print("Role: Admin")