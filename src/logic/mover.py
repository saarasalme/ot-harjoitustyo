import time

class Mover():
    """Class for handling movement of entities on the screen"""

    def __init__(self):
        self.speed = 3
        self.width = 40
        self.height = 41

    def move_roni(self, left, right, down, up, roni_x, roni_y):
        """ This method moves the player 
        Args:
        left - boolean representing if the player is moving left
        right - boolean representing if the player is moving right
        down - boolean representing if the player is moving down
        up - boolean representing if the player is moving up
        roni_x - players x_coordinate
        roni_y - payers y_coordinate
        """
        if left:
            if roni_x > 0:
                roni_x -= self.speed
        if right:
            if roni_x < 640 - self.width:
                roni_x += self.speed
        if down:
            if roni_y < 480 - self.height:
                roni_y += self.speed
        if up:
            if roni_y > 0:
                roni_y -= self.speed
        return roni_x, roni_y

    def move_snack(self, coordinates: list):
        """ This method moves snacks
        Args:
        coordinates - the x and y coordinates of the snack"""
        now = time.localtime()
        seconds = time.strftime("%S", now)
        if int(seconds) % 2 == 0:
            if coordinates[2] == "go_down":
                coordinates[0] += 1
                coordinates[1] += 2
            if coordinates[2] == "go_up":
                coordinates[0] += 1
                coordinates[1] -= 2
            if coordinates[2] == "go_left":
                coordinates[0] -= 2
                coordinates[1] += 1
            if coordinates[2] == "go_right":
                coordinates[0] += 2
                coordinates[1] += 1
        else:
            if coordinates[2] == "go_down":
                coordinates[0] -= 1
                coordinates[1] += 2
            if coordinates[2] == "go_up":
                coordinates[0] -= 1
                coordinates[1] -= 2
            if coordinates[2] == "go_left":
                coordinates[0] -= 2
                coordinates[1] -= 1
            if coordinates[2] == "go_right":
                coordinates[0] += 2
                coordinates[1] -= 1
        
        return coordinates
