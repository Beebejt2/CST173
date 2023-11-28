
from DiceClass import Dice

dice1 = Dice(input("How many sides?: "))
for x in range(0,10):
    if x < 9:
        print(dice1.roll(), end=", ")
    else:
        print(dice1.roll())
