import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti1 = Maksukortti(1000)
        self.maksukortti2 = Maksukortti(100)

    def test_lahtokassa_tuhat(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulisia_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaita_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateinen_riittaa_edullinen_kassasaldo_lounaat(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateinen_riittaa_edullinen_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_kateinen_ei_riita_edullinen_kassasaldo_lounaat(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateinen_ei_riita_edullinen_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kateinen_riittaa_maukas_kassasaldo_lounaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateinen_riittaa_maukas_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kateinen_ei_riita_edullinen_kassasaldo_lounaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateinen_ei_riita_maukas_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_kortilla_rahaa_edullinen_saldo(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti1)
        self.assertEqual(self.maksukortti1.saldo, 760)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti1), True)

    def test_kortilla_rahaa_edullinen_lounaat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti1)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti1), True)

    def test_saldo_ei_riita_edullinen_saldo(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)
        self.assertEqual(self.maksukortti2.saldo, 100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2), False)

    def test_saldo_ei_riita_edullinen_lounaat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2), False)

    def test_kortilla_rahaa_maukas_saldo(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti1)
        self.assertEqual(self.maksukortti1.saldo, 600)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti1), True)

    def test_kortilla_rahaa_maukas_lounaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti1)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti1), True)

    def test_saldo_ei_riita_maukas_saldo(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)
        self.assertEqual(self.maksukortti2.saldo, 100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2), False)

    def test_saldo_ei_riita_maukas_lounaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2), False)

    def test_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_kortti(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti1, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(self.maksukortti1.saldo, 2000)

    def test_lataa_kortti_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti1, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti1.saldo, 1000)