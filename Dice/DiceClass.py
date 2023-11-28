import random
class Dice:

    def __init__(self, sides):
        self.sides = int(sides)
        
    def roll(self):
        return random.randint(1, self.sides)        
