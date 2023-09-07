class User:

    def __init__(self, name, last_name, age, eye_color):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.eye_color = eye_color
        self.login_attempts = 0

    def describe_user(self):
        print(f"You are: {self.name} {self.last_name}, {self.age} y.o. You have {self.eye_color} color of eyes.")

    def greet_user(self):
        print(f"Welcome, {self.name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

