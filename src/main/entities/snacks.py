from random import randint, choice

class Snacks:
    """ Class to create snacks """

    def __init__(self):
        """ The class constructor """
        self.snacks = []


    def add_snack(self, level):
        """ This method creates snacks in random places around the screen """
        chance = randint(0,60)
        if chance == 0:
            from_up = [randint(0, 640), -20, "go_down", randint(1,level+1)]
            from_right = [660, randint(0, 480), "go_left", randint(1,level+1)]
            from_down = [randint(0, 640), 500, "go_up", randint(1,level+1)]
            from_left = [-20, randint(0, 480), "go_right", randint(1,level+1)]
            direction = choice([from_up, from_right, from_left, from_down])
            self.snacks.append(direction)