from random import randint, choice


class Snacks:
    def __init__(self):
        self.sausages = []
        self.meatballs = []
        self.treats = []

    def add_snack(self):
        snack = choice([self.sausages, self.meatballs, self.treats])
        from_up = [randint(0, 640), -20]
        from_right = [660, randint(0, 480)]
        from_down = [randint(0, 640), 500]
        from_left = [-20, randint(0, 480)]
        direction = choice([from_up, from_right, from_left, from_down])
        snack.append(direction)
        