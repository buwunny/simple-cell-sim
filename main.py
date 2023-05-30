import numpy as np
import matplotlib.pyplot as plt
import random as rand
import pygame

class Cell:
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
        self.collider = pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
        self.location = [self.x, self.y]
        self.count += 1
        if self.count == 60:
            self.starving_days += 1
            self.count = 0

        if self.starving_days >= 5:
            self.alive = False
            corpse_pos = agar.agar[self.y][self.x]
            corpse_pos.nutrient = self.size
            corpse_pos.food_color = (0, 100, 0)
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
        r = Cell(int(self.size/2), self.x - 5, self.y)
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
        self.food = False

        self.food_color = (0, 255, 0)
        self._collider = pygame.Rect(self.x, self.y, self.nutrient, self.nutrient)
    
    @property
    def collider(self):
        return pygame.Rect(self.x - self.nutrient, self.y - self.nutrient, self.nutrient * 2 , self.nutrient * 2)

    def harvest(self):
        self.nutrient -= 1


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

if __name__ == "__main__":
    w = 1920
    h = 1080
    

    cell_data = []
    food_data = []
    nutrient_data = []
    timestamps = []

    pygame.init()
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    agar = Agar(w, h)
    agar.add_food(500)
    cells = [Cell(5, int(w/2), int(h / 2))]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if len(cells) == 0:
            running = False

        screen.fill(0)

        for f in agar.foods:
            pygame.draw.circle(screen, f.food_color, [f.x, f.y], f.nutrient)
            if f.nutrient <= 0:
                agar.foods.remove(f)

        for i in cells:
            if not i.alive:
                cells.remove(i)
            pygame.draw.circle(screen, "red", i.location, i.size)
            for f in agar.foods:
                if f.collider.colliderect(i.collider):
                    f.harvest()
                    i.eat()

        for i in range(0, len(cells)):
            i = cells[i]
            a = i.update(agar)
            if (a != 0):
                cells.append(a)
        
        pygame.display.flip()
        
        cell_data.append(len(cells))
        food_data.append(len(agar.foods))
        timestamps.append(pygame.time.get_ticks() / 1000)

        clock.tick(60)

    pygame.quit()

    x = np.array(timestamps)

    y = np.array(cell_data)
    plt.plot(x, y, color="red", label="number of cells")
    y = np.array(food_data)
    plt.plot(x, y, color="green", label="number of food sources")

    plt.xlabel("Time (seconds)")
    plt.legend(loc="upper right")
    plt.show()
    