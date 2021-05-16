import unittest
from main.logic.mover import Mover

class TestMover(unittest.TestCase):
    def setUp(self):
        self.mover = Mover()

    def test_move_roni_left(self):
        new_coordinates = self.mover.move_roni(True, False, False, False, 3, 0, 1)
        self.assertEqual(new_coordinates, (0,0))

    def test_not_out_of_screen_left(self):
        new_coordinates = self.mover.move_roni(True, False, False, False, 1, 0, 1)
        self.assertEqual(new_coordinates, (1,0))

    def test_move_roni_right(self):
        new_coordinates = self.mover.move_roni(False, True, False, False, 0, 0, 1)
        self.assertEqual(new_coordinates, (3,0))

    def test_not_out_of_screen_right(self):
        new_coordinates = self.mover.move_roni(False, True, False, False, 640 - self.mover.sizes[0][0], 0, 1)
        self.assertEqual(new_coordinates, (640 - self.mover.sizes[0][0], 0))

    def test_move_roni_down(self):
        new_coordinates = self.mover.move_roni(False, False, True, False, 0, 0, 1)
        self.assertEqual(new_coordinates, (0,3))
    
    def test_not_out_of_screen_down(self):
        new_coordinates = self.mover.move_roni(False, False, True, False, 0, 480 - self.mover.sizes[0][1], 1)
        self.assertEqual(new_coordinates, (0,480 - self.mover.sizes[0][1]))

    def test_move_roni_up(self):
        new_coordinates = self.mover.move_roni(False, False, False, True, 0, 3, 1)
        self.assertEqual(new_coordinates, (0,0))

    def test_not_out_of_screen_up(self):
        new_coordinates = self.mover.move_roni(False, False, False, True, 0, 2, 1)
        self.assertEqual(new_coordinates, (0, 2))