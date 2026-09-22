from student import Student
from mentor import Mentor
from admin import Admin
users = [
    Student(101, "Rajesh", "rajesh@gmail.com"),
    Mentor(201, "Parimala", "parimala@gmail.com"),
    Admin(301,, "Ritik", "ritik@gmail.com")
]

for user in users:
    user.display_details()
    print()