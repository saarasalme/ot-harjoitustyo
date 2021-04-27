import time

class Mover():
    def move_roni(self):
        if self.left:
            if self.roni_x > 0:
                self.roni_x -= self.speed
        if self.right:
            if self.roni_x < 640 - self.roni.get_width():
                self.roni_x += self.speed
        if self.down:
            if self.roni_y < 480 - self.roni.get_height():
                self.roni_y += self.speed
        if self.up:
            if self.roni_y > 0:
                self.roni_y -= self.speed

    def move_snack(self, coordinates: list):
        now = time.localtime()
        seconds = time.strftime("%S", now)
        if int(seconds) % 6 < 3:
            if coordinates[2] == "go_down":
                coordinates[0] += 2
                coordinates[1] += 3
            if coordinates[2] == "go_up":
                coordinates[0] += 2
                coordinates[1] -= 3
            if coordinates[2] == "go_left":
                coordinates[0] += 3
                coordinates[1] += 2
            if coordinates[2] == "go_right":
                coordinates[0] -= 3
                coordinates[1] += 2
        else:
            if coordinates[2] == "go_down":
                coordinates[0] -= 2
                coordinates[1] += 3
            if coordinates[2] == "go_up":
                coordinates[0] -= 2
                coordinates[1] -= 3
            if coordinates[2] == "go_left":
                coordinates[0] += 3
                coordinates[1] -= 2
            if coordinates[2] == "go_right":
                coordinates[0] -= 3
                coordinates[1] -= 2
        
        return coordinates

m = Mover()
koordinaatit = [0,100, "go_right"]
print(m.move_snack(koordinaatit))