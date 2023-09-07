class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriotive_name(self):
        long_name = f"{self.year} {self.brand} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Use more than 0")

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

my_tesla = ElectricCar('Tesla', 'model s', 2021)
print(my_tesla.get_descriotive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()




# my_new_car.odometer_reading = 25
# my_new_car.read_odometer()

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriotive_name())
#
# my_new_car.update_odometer(5)
#
# my_new_car.read_odometer()

