from user import User
class Privileges():

    def __init__(self, privileges=('add post', 'delete post', 'ban user')):
        self.privileges = privileges

    def show_privileges(self):
        print(f"This user is an Admin. He can: {self.privileges}.")

class Admin(User):

    def __init__(self, name, last_name, age, eye_color):
        super().__init__(name, last_name, age, eye_color)
        self.privileges = Privileges()