from random import randint, choice

class Snacks:
    def __init__(self):
        self.sausages = []
        self.meatballs = []
        self.treats = []

    def add_snack(self):
        chance = randint(0,100)
        if chance == 0:
            snack = choice([self.sausages, self.meatballs, self.treats])
            from_up = [randint(0, 640), -20, "go_down"]
            from_right = [660, randint(0, 480), "go_left"]
            from_down = [randint(0, 640), 500, "go_up"]
            from_left = [-20, randint(0, 480), "go_right"]
            direction = choice([from_up, from_right, from_left, from_down])
            snack.append(direction)