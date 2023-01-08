import random

class Balle:
    def __init__(self):
        self.x = random.randint(30, 770)
        self.y = 50
        sensx = random.randint(0, 1)
        if sensx == 0:
            self.speedx = 5
        else:
            self.speedx = -5
        self.speedy = 0
        self.color = random.randint(0,4)
