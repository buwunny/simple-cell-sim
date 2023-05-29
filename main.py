import numpy as np
import matplotlib.pyplot as plt
import random as rand
import pygame

class Snuggle:
    def __init__(self, start_size, start_hunger, start_thirst, start_x, start_y):
        self.size = start_size
        self.locations = [[start_x, start_y]]
        self.hunger = start_hunger
        self.thirst = start_thirst
        self.day = 0
        self.starving_days = 0
        self.thirsting_days = 0

        # life(day)

    def update(self, agar):
        l = len(self.locations)
        for i in range(0, l):
            pos = self.locations[i]
            new_pos = agar.get_adjacent(pos[0], pos[1])
            for i in new_pos:
                if not i.alive:
                    sec = agar.agar[i.y][i.x]
                    sec.alive = True
                    sec.change = True
                    self.locations.append([i.x, i.y])

        # self.locations.append(self.makeDecision(self.hunger, self.thirst))
        # self.update_vitals()
        
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
        self.food = False
        self.water = False
        self.alive = False
        self.change = False

        self._color = (0, 0, 0)

    @property
    def color(self):
        if self.alive:
            return (255, 0, 0)
        if self.food:
            return (0, 255, 0)
        if self.water:
            return (0, 0, 255)
    

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
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.agar = [[Section(i, j) for i in range(self.width)] for j in range(self.height)]

    def add_food(self, n):
        for _ in range(0, n):
            x = rand.randint(0, self.width-1)
            y = rand.randint(0, self.height-1)
            sec = self.agar[y][x]
             
            sec.nutrient = 100
            sec.food = True
            sec.change = True
            
            for i in self.get_adjacent(x, y):
                if i.nutrient == 0:
                    i.nutrient += 50
                    i.food, i.change = True, True
                for j in self.get_adjacent(i.x, i.y):
                    if j.nutrient == 0:
                        j.nutrient += 25
                        j.food, j.change = True, True

    def see_food(self):
        a = []
        for row in self.agar:
            for column in row:
                if column.nutrient != 0:
                    a.append([column.x, column.y])
        return a
                
    # def add_water(self, n):
    #     for i _ in range(n):
    #         self.agar[rand.randint(0, len(agar))][rand.randint(0, len(agar[]))].water(100)



    def get_adjacent(self, x, y):
        l = []
        if y + 1 < self.height:
            l.append(self.agar[y+1][x])
        if y - 1 > 0:
            l.append(self.agar[y-1][x])
        if x + 1 < self.width:
            l.append(self.agar[y][x+1])
        if x - 1 > 0:
            l.append(self.agar[y][x-1])
        return l



    

if __name__ == "__main__":
    w = 1920
    h = 1080
    
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    agar = Agar(w, h)
    guy = Snuggle(0, 0, 0, 100, 100)

    # player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    running = True
    start = True
    while running:

        if start:
            
            screen.fill(0)
            agar.add_food(50)
            start = False

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pixel_array = pygame.PixelArray(screen)

        for r in agar.agar:
            for c in r:
                if c.change:
                    pixel_array[c.x, c.y] = c.color        
                    c.change = False

        pixel_array.close()
        
        # pygame.draw.circle(screen, "red", player_pos, 40)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            guy.update(agar)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()