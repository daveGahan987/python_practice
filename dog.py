class Dog:
    """Single class to create Dog"""

    def __init__(self, name, age):
        "Initiate attributes name and age."
        self.name = name
        self.age = age

    def sit(self):
        """Simulate 'sitting' command."""
        print(f"{self.name} is name sitting.")

    def roll_over(self):
        """Simulate 'roll over' command."""
        print(f"{self.name} is now rolling over.")


my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

