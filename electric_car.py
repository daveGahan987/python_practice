from car import Car

class Battery():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Your car has {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            print("Your car can go 250 km")
        elif self.battery_size == 100:
            print("Your car can go 320 km")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print('Your battery now is full charged')
        else:
            print("Your battery is already full charged. Can't upgrade it.")


class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.battery = Battery()