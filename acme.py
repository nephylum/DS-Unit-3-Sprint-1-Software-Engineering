"""
Set up the Class 'Product' with the following attributes
name (no default)
price (int with default value of 10)
weight (integer with default value of 20)
flammability (float with default value of 0.5)
indentifier (integer, automatically generated as a random (uniform) number
anywhere from 1,000,000 to 9,999,999)
"""
import random


class Product():

    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        pw_ratio = self.price / self.weight
        if (pw_ratio < 0.5):
            return "Not so stealable..."
        elif (pw_ratio > 0.5 and pw_ratio < 1.0):
            return "Kinda stealable."
        else:
            return "Very Stealable"

    def explode(self):
        boomratio = self.flammability * self.weight
        if (boomratio < 10):
            return "...fizzle"
        elif (boomratio >= 10 and boomratio < 50):
            return "...boom!"
        else:
            return "...BABOOM!"


class BoxingGlove(Product):
    def __init__(self, name='Bob'):
        self.weight = 10
        self.name = name
        self.price = 10
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if (self.weight < 5):
            return "That tickles."
        elif (self.weight >= 5 and self.weight < 15):
            return "Hey that hurt!"
        else:
            return "OUCH!"
