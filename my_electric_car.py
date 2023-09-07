from car import ElectricCar

my_beetle = ElectricCar('volkswagen', 'beetle', 2020)
print(my_beetle.get_descriptive_name())
my_beetle.battery.describe_battery()
my_beetle.battery.get_range()

