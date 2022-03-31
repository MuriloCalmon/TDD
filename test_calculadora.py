import unittest
from calculadora import soma, subtrai


class TesteCalculadora(unittest.TestCase):
    def test_soma_20_e_20_deve_retornar_40(self):
        self.assertEqual(soma(20, 20), 40)

    def test_soma_15_negativo_e_10_deve_retornar_5_negativo(self):
        self.assertEqual(soma(-15, 10), -5)

    def test_soma_varias_entradas(self):
        a_b_saidas = (
            (1500, 1200, 2700),
            (-1500, 1200, -300),
            (15, 15, 30),
            (-2, 2, 0),
        )

        for a_b_saida in a_b_saidas:
            with self.subTest(a_b_saida=a_b_saida):
                a, b, saida = a_b_saida
                self.assertEqual(soma(a, b), saida)

    def test_soma_a_precisa_ser_int_ou_float_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('a', 5)

    def test_soma_b_precisa_ser_int_ou_float_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(10, '5')

    def test_subtrai_50_e_20_deve_retornar_30(self):
        self.assertEqual(subtrai(50, 20), 30)

    def test_subtrai_10_negativo_e_15_negativo_deve_retornar_5(self):
        self.assertEqual(subtrai(-10, -15), 5)

    def test_subtrai_varias_entradas(self):
        a_b_saidas = (
            (5000, 200, 4800),
            (-500, -500, 0),
            (30, 20, 10),
            (12, 4, 8),
            (17, 10, 7),
        )

        for a_b_saida in a_b_saidas:
            with self.subTest(a_b_saida=a_b_saida):
                a, b, saida = a_b_saida
                self.assertEqual(subtrai(a, b), saida)

    def test_subtrai_a_precisa_ser_int_ou_float_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai('50', 5)

    def test_subtrai_b_precisa_ser_int_ou_float_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai(10, '2')


if __name__ == "__main__":
    unittest.main(verbosity=2)
