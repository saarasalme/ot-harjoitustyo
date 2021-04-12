import unittest
from RoniPoika import Snacks


class TestGame(unittest.TestCase):
    def setUp(self):
        self.snacks = Snacks()

    def test_meatballs_exists(self):
        self.assertIsNotNone(self.snacks.meatballs)

    def test_sausages_exists(self):
        self.assertIsNotNone(self.snacks.sausages)

    def test_treats_exists(self):
        self.assertIsNotNone(self.snacks.treats)

        
    