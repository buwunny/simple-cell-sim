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



class Pocket:
    def __init__(self, nutrient, humidity, light):
        self.nutrient = nutrient
        self.humidity = humidity
        self.light = light

    def harvest()

    

if __name__ == "main":
    
    agar = [[Pocket(0, 0, 0) for _ in range(10)] for _ in range(10) ]
    s = Snuggle(1, 10, 10)

