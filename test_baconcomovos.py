"""
TDD - Teste driven development

Red
Parte 1 -> Criar o teste e ver falhar

Green
Parte 2 -> Criar o código e ver o teste passar

Refactor
Parte 3 -> Melhorar meu código
bco = bacon_com_ovos
"""
import unittest
from baconcomovos import bacon_com_ovos


class TesteBaconComOvos(unittest.TestCase):
    def test_bco_deve_levantar_assertionError_se_o_numero_n_for_inteiro(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')

    def test_bco_deve_retornar_bco_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                                 msg=f' "{entrada}", não retornou "{saida}"')

    def test_bco_deve_retornar_passar_fome_se_nao_for_multiplo_de_3_e_5(self):
        entradas = (22, 32, 56, 98)
        saida = 'Passa fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                                 msg=f'"{entrada}", não retorno "{saida}" ')

    def test_bco_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                                 msg=f'"{entrada}", não retorno "{saida}" ')

    def test_bco_deve_retornar_ovos_se_entrada_for_multiplo_de_5(self):
        entradas = (5, 10, 25, 35, 50, 55, 70)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                                 msg=f'"{entrada}", não retorno "{saida}" ')


if __name__ == "__main__":
    unittest.main(verbosity=2)
