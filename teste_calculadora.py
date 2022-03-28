import unittest
from calculadora import soma

class TesteCalculadora(unittest.TestCase):
    def test_soma_20_e_20_deve_retornar_40(self):
        self.assertEqual(soma(20, 20), 40)

    def test_soma_15_negativo_e_10_deve_retornar_5_negativo(self):
        self.assertEqual(soma(-15, 10), -5)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (1500, 1200, 2700),
            (-1500, 1200, -300),
            (15, 15, 30),
            (-2, 2, 0),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)


    def test_x_precisa_ser_int_ou_float_deve_retornat_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('a', 5)

    def test_y_precisa_ser_int_ou_float_deve_retornat_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(10, '5')
            


unittest.main(verbosity=2)
