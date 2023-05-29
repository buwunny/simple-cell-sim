import numpy as np
import matplotlib.pyplot as plt
import random as rand
import pygame

class Snuggle:
    def __init__(self, start_size, start_x, start_y):
        self.size = start_size
        self.locations = [[start_x, start_y]]
        self.hunger = 100
        self.thirst = 100       
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


class Rawr:
    def __init__(self, start_size, start_x, start_y):
        self.alive = True
        self.size = start_size
        self.x = start_x
        self.y = start_y
        self.split_size = 10
        self.collider = pygame.Rect(start_x - start_size, start_y - start_size, start_size * 2, start_size * 2)
        self.location = [start_x, start_y]
        self.starving_days = 0
        self.count = 0

    def update(self, agar):
        # if self.alive:
        self.collider = pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
        self.location = [self.x, self.y]
        self.count += 1
        if self.count == 60:
            print(self.starving_days)
            self.starving_days += 1
            self.count = 0

        if self.starving_days >= 5:
            self.alive = False
            corpse_pos = agar.agar[self.y][self.x]
            corpse_pos.nutrient = self.size * 0.7
            corpse_pos.food = True
            agar.foods.append(corpse_pos)
            self.size = 0

        self.random_move(agar)
        if self.size >= self.split_size:
            return self.split()
        else:
            return 0


    def random_move(self, agar):
        delta_x = rand.randint(0, 20) * rand.randint(-1, 1)
        delta_y = rand.randint(0, 20) * rand.randint(-1, 1)
        if (self.x + delta_x < agar.width - self.size and self.x + delta_x > self.size
            and
            self.y + delta_y < agar.height - self.size and self.y + delta_y > self.size):
            self.x += delta_x
            self.y += delta_y

    def split(self):
        r = Rawr(int(self.size/2), self.x - 5, self.y)
        self.size /= 2
        self.x += 5
        return r

    def eat(self):
        self.size += 0.7
        self.starving_days = 0

class Section:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nutrient = 0
        self.water = 0
        self.light = 0
        self.food = False
        self.water = False
        self.change = False

        self._color = (0, 0, 0)
        self._collider = pygame.Rect(self.x, self.y, self.nutrient, self.nutrient)

    @property
    def color(self):
        if self.food:
            return (0, 255, 0)
        if self.water:
            return (0, 0, 255)
        else:
            return (0, 0, 0)
    
    @property
    def collider(self):
        return pygame.Rect(self.x - self.nutrient, self.y - self.nutrient, self.nutrient * 2 , self.nutrient * 2)

    

    def harvest(self):
        self.nutrient -= 1


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
        self.foods = []

    def add_food(self, n):
        for _ in range(0, n):
            x = rand.randint(0, self.width-1)
            y = rand.randint(0, self.height-1)
            sec = self.agar[y][x]
            self.foods.append(sec)
            sec.nutrient = 10 * (rand.randint(5, 10) / 10)
            sec.food = True
            sec.change = True
            

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
    # guy = Snuggle(0, int(w/2), int(h / 2))
    b = [Rawr(5, int(w/2), int(h / 2))]

    # player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    running = True
    start = True
    while running:

        if start:
            
            agar.add_food(500)
            start = False

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(0)
        for f in agar.foods:
            if f.nutrient <= 0:
                agar.foods.remove(f)
            # pygame.draw.rect(screen, "white", f.collider)
            pygame.draw.circle(screen, f.color, [f.x, f.y], f.nutrient)

        # pygame.draw.rect(screen, "white", guy.collider)
        for i in b:
            if not i.alive:
                b.remove(i)
            pygame.draw.circle(screen, "red", i.location, i.size)

        
        
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        for o in b:
            for food in agar.foods:
                if food.collider.colliderect(o.collider):
                    food.harvest()
                    o.eat()

        # flip() the display to put your work on screen
        pygame.display.flip()

        # for o in range(0, len(b)):
        #     b[o]
        #     b
        for i in range(0, len(b)):
            i = b[i]
            a = i.update(agar)
            if (a != 0):
                b.append(a)
                
        clock.tick(60)

    pygame.quit()