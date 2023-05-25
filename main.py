import numpy as np
import matplotlib.pyplot as plt
import random as rand

class Snuggle:
    def __init__(self, start_size, start_hunger, start_thirst, start_x, start_y):
        self.size = start_size
        self.locations = [[start_x, start_y]]

        self.hunger = start_hunger
        self.thirst = start_thirst
        self.day = 0
        self.starving_days = 0
        self.thirsting_days = 0

        life(day)

    def update(self, agar):
        self.locations.append(self.makeDecision(self.hunger, self.thirst))
        self.update_vitals()
        
        # if self.is_alive:
        #     life(day += 1)
    
    def is_alive(self, starving_days, thirsting_days):
        if starving_days >= 7:
            return False 
        if thirsting_days >= 3:
            return False
        return True

    def update_vitals(self, gathered_food, gathered_moisture):
        self.hunger -= 1
        self.thirst -= 1
        
        self.hunger += gathered_food
        self.food += gathered_moisture

        # self.starving_days += 1 if self.hunger <= 0 else self.starving_days = 0
        # self.thirsting_days += 1 if self.thirst <= 0 else self.thirsting_days = 0

    def display(self):
        return

    def get_next_decision(self):
    
        return

    def find_highest_desireability(self):
        # for l in self.locations:
             
        return


class Section:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nutrient = 0
        self.water = 0
        self.light = 0
        self.source = False
        self.contains_bacteria = False

    def harvest(self):
        return
    


"""
SOURCE DISTRIBUTIONS
S 0.1 100%
A 0.2 90%
B 0.4 80%
C 0.2 70%
D 0.1 60%
"""
class Agar:
    def __init__(self, size):
        self.size = size
        self.agar = [[Section(i, j) for i in range(self.size)] for j in range(self.size)]

    def add_food(self, n):
        l = self.size-1
        for _ in range(0, n):
            x = rand.randint(0, l)
            y = rand.randint(0, l)
            self.agar[y][x].nutrient = 100
            for i in self.get_adjacent(x, y):
                if i.nutrient == 0:
                    i.nutrient += 50
                for j in self.get_adjacent(i.x, i.y):
                    if j.nutrient == 0:
                        j.nutrient += 25
        self.agar[0][0].nutrient = -100

    def see_food(self):
        a = []
        for row in self.agar:
            b = []
            for column in row:
                if column != -100:
                    b.append(column.nutrient)
                else:
                    b.append(-100)
            a.append(b)
        return a
    # def add_water(self, n):
    #     for i _ in range(n):
    #         self.agar[rand.randint(0, len(agar))][rand.randint(0, len(agar[]))].water(100)


    def spread_resources(self, amount):
        return



    def get_adjacent(self, x, y):
        l = []
        if y + 1 < self.size:
            l.append(self.agar[y+1][x])
        if y - 1 >= 0:
            l.append(self.agar[y-1][x])
        if x + 1 < self.size:
            l.append(self.agar[y][x+1])
        if x - 1 >= 0:
            l.append(self.agar[y][x-1])
        return l



    

if __name__ == "__main__":
    agar = Agar(50)
    
    agar.add_food(50)
    A = np.array(agar.see_food())
    # agarf.add_water(10)

    # b = Bacteria(1, 50, 50, 500, 500)
    # while True:
    #     b.update(agar)

    # H = np.array([[rand.randint(0, 100) for _ in range(0, 1000)] for _ in range(0, 1000)])
    

    plt.imshow(A, interpolation='bilinear')
    
    
    plt.show()

"""
o
"""