from admin_user import Admin

# user_1 = User('Sonny', 'Corleone', 38, 'brown')
# user_2 = User('Michael', 'Corleone', 32, 'black')
user_3 = Admin('Don', 'Corleone', 65, 'brown')

# user_1.greet_user()
# user_1.describe_user()
# user_2.greet_user()
# user_2.describe_user()
user_3.greet_user()
user_3.describe_user()

user_3.privileges.show_privileges()
