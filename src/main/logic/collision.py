class Collision:
    """ Class to check if snacks needs to be removed """

    def __init__(self):
        """ The class constructor """

        self.snack_sizes = [(18,20),(23,40),(29,55),(95,50)]
        self.roni_sizes = [(63,40),(79,50),(88,60),(0,0)]

    def if_hits(self, coordinates, roni_x, roni_y, level):
        """ Method to check if player hit snack 

        Args: 
            coordinates - snack coordinates
            roni_x - players x coordinate
            roni_y - players y coordinate
            level - the level of the game
            
        Returns:
            True, if player hits snack, False in other cases.
        """

        did_hit = False
        if roni_x + 5 <= coordinates[0] + self.snack_sizes[coordinates[3]-1][0] and roni_x + self.roni_sizes[level-1][0] -5 >= coordinates[0]:
            if roni_y + 5 <= coordinates[1] + self.snack_sizes[coordinates[3]-1][1] and roni_y + self.roni_sizes[level-1][1] -5 >= coordinates[1]:
                did_hit = True
        return did_hit

    def if_out_of_screen(self, coordinates):
        """ Method to check if the snack is out of screen

        Args:
            coordinates - snack coordinates

        Returns:
            True if the snack is out of screen, False in other cases
        """

        is_out = False
        if coordinates[0] > 700 or coordinates[0] < -100:
            is_out = True
        if coordinates[1] > 600 or coordinates[1] < -100:
            is_out = True
        return is_out 

