class User:
    def init(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def display_details(self):
        print(f" ID: {self.user_id}")
        print(f" Name: {self.name}")
        print(f" Email:" {self.email})