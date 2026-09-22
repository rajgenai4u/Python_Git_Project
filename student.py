from user import User
class Student(User):
    def display_details(self):
        super().display_details()
        print("Role: Student")
        print("Access: Learning Dashboard")
