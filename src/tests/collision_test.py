import unittest
from main.logic.collision import Collision


class TestCollision(unittest.TestCase):
    def setUp(self):
        self.collision = Collision()

    def test_snack_sizes_exist(self):
        self.assertEqual(len(self.collision.snack_sizes), 4)

    def test_roni_sizes_exist(self):
        self.assertEqual(len(self.collision.roni_sizes), 4)

    def test_if_hits_True(self):
        self.assertTrue(self.collision.if_hits([0,0,"x",1],0,0,1))

    def test_if_hits_False(self):
        self.assertFalse(self.collision.if_hits([0,0,"x",1],100,100,1))

    def test_if_out_of_screen_True(self):
        self.assertTrue(self.collision.if_out_of_screen([800,0]))
        self.assertTrue(self.collision.if_out_of_screen([-150,0]))
        self.assertTrue(self.collision.if_out_of_screen([0,700]))
        self.assertTrue(self.collision.if_out_of_screen([0,-150]))

    def test_if_out_of_screen_False(self):
        self.assertFalse(self.collision.if_out_of_screen([10,10]))
