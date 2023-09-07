from car import Car
from electric_car import ElectricCar as EC

my_beetle = EC('volkswagen', 'beetle', 2020)
print(my_beetle.get_descriptive_name())
my_beetle.battery.describe_battery()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())