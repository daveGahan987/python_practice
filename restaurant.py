class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant {self.name} has {self.cuisine} type of cuisine. Now is {self.number_served} people here.")

    def open_restaurant(self):
        print(f"Restaurant {self.name} is now opened.")

    def set_number_served(self, count):
        self.number_served = count
        print(f"Number of users has been changed on: {self.number_served}.")

    def increment_number_served(self, count):
        self.number_served += count
        print(f"Number of users has been incremented by {count}. Now is {self.number_served} people here.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def get_flavors(self):
        print(f"In restaurant {self.name} you can find {self.flavors} flavors of ice cream.")