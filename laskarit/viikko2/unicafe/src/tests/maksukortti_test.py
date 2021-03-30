import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_saldon_kasvatus_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_saldo_vahenee_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahat_riittävät(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_rahat_ei_riitä(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)     
