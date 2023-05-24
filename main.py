import random as rand

class Snuggle:
    def __init__(self, start_size, start_hunger, start_thirst):
        self.size = start_size
        self.locations = [[500, 500]]

        self.hunger = start_hunger
        self.thirst = start_thirst
        self.day = 0
        self.starving_days = 0
        self.thirsting_days = 0

        life(day)

    def life(self, day):        
        self.location.append(self.makeDecision(self.hunger, self.thirst))
        self.update_vitals()
        
        if self.is_alive:
            life(day += 1)
    
    def is_alive(self, starving_days, thirsting_days):
        if starving_days >= 7 return False 
        if thirsting_days >= 3 return False
        return True

    def update_vitals(self, gathered_food, gathered_moisture):
        self.hunger -= 1
        self.thirst -= 1
        
        self.hunger += gathered_food
        self.food += gathered_moisture

        self.starving_days += 1 if self.hunger <= 0 else self.starving_days = 0
        self.thirsting_days += 1 if self.thirst <= 0 else self.thirsting_days = 0

    def display(self):
        return

    def get_next_decision(self):
    
        return

    def find_highest_desireability()
        return


class Section:
    def __init__(self, nutrient, water, light):
        self._nutrient = nutrient
        self._water = water
        self.light = light
        self._source = False

    def harvest(self):
        return
    
    @property
    def nutrient(self):
        return self._x

    @nutrient.setter
    def nutrient(self, n):
        self._nutrient = n

    @property
    def water(self):
        return self._x

    @water.setter
    def water(self, w):
        self._water = w

    @property
    def source(self):
        return self.source
    
    @source.setter
    def source(self, s):
        self._source = s


"""
SOURCE DISTRIBUTIONS
S 0.1 
A 0.2
B 0.4
C 0.2
D 0.1
"""
class Agar:
    def __init__(self):
        self.agar = [[Section(0, 0, 0) for _ in range(20)] for _ in range(20)]

    def add_food(self, n):
        for i _ in range(n):
            self.agar[rand.randint(0, len(agar))][rand.randint(0, len(agar[]))].nutrient(100)

    def add_water(self, n):
        for i _ in range(n):
            self.agar[rand.randint(0, len(agar))][rand.randint(0, len(agar[]))].water(100)

    def spread_resources(self, amount):



    

if __name__ == "main":
    
agar = Agar()
agar.add_food(10)
agarf.add_water(10)

"""
o
"""