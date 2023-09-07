from random import randint

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for a in range(10):
            print(randint(1, self.sides))