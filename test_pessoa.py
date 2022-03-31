"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obitidos bool

    API:
        obter_todos_os_dados -> method
            OK
            404
"""
import unittest
from unittest.mock import patch
from pessoas import Pessoa


class TestePessoa(unittest.TestCase):

    def setUp(self):
        self.nomes = ('Murilo', 'Esther', 'Igor')
        self.sobrenomes = ('Calmon', 'Silva', "Santos")
        self.pessoa1 = Pessoa('Murilo', 'Calmon')
        self.pessoa2 = Pessoa('Esther', 'Silva')
        self.pessoa3 = Pessoa('Igor', 'Santos')
        self.pessoas = (self.pessoa1, self.pessoa2, self.pessoa3)

    def teste_pessoa_attr_nome_tem_o_valor_correto(self):

        for pessoa in self.pessoas:
            if pessoa.nome == self.nomes[0]:
                self.assertEqual(pessoa.nome, 'Murilo')
            if pessoa.nome == self.nomes[1]:
                self.assertEqual(pessoa.nome, 'Esther')
            if pessoa.nome == self.nomes[2]:
                self.assertEqual(pessoa.nome, 'Igor')

    def teste_pessoa_attr_nome_e_str(self):
        for pessoa in self.pessoas:
            if pessoa.nome == 'Murilo':
                self.assertIsInstance(pessoa.nome, str)
            if pessoa.nome == 'Esther':
                self.assertIsInstance(pessoa.nome, str)
            if pessoa.nome == 'Igor':
                self.assertIsInstance(pessoa.nome, str)

    def teste_pessoa_attr_sobrenome_e_str(self):
        for pessoa in self.pessoas:
            if pessoa.sobrenome == 'Calmon':
                self.assertIsInstance(pessoa.sobrenome, str)
            if pessoa.sobrenome == 'Silva':
                self.assertIsInstance(pessoa.sobrenome, str)
            if pessoa.sobrenome == 'Santos':
                self.assertIsInstance(pessoa.sobrenome, str)

    def teste_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        for pessoa in self.pessoas:
            if pessoa.sobrenome == self.sobrenomes[0]:
                self.assertEqual(pessoa.sobrenome, 'Calmon')
            if pessoa.sobrenome == self.sobrenomes[1]:
                self.assertEqual(pessoa.sobrenome, 'Silva')
            if pessoa.sobrenome == self.sobrenomes[2]:
                self.assertEqual(pessoa.sobrenome, 'Santos')

    def teste_pessoa_attr_se_dados_obtidos_e_false(self):
        for pessoa in self.pessoas:
            self.assertFalse(pessoa.dados_obtidos)

    def teste_obter_todos_os_dados_ok(self):
        with patch('requests.get') as requests_fake:
            requests_fake.return_value.ok = True

            for pessoa in self.pessoas:

                self.assertAlmostEqual(pessoa.obter_todos_os_dados(), 'Co\
                    nectado')
                self.assertTrue(pessoa.dados_obtidos)

    def teste_obter_todos_os_dados_erro_404(self):
        with patch('requests.get') as requests_fake:
            requests_fake.return_value.ok = False

            for pessoa in self.pessoas:

                self.assertAlmostEqual(pessoa.obter_todos_os_dados(), 'E\
                    rro 404')
                self.assertFalse(pessoa.dados_obtidos)

    def teste_obter_todos_os_dados_sucesso_falha_sequencial(self):
        with patch('requests.get') as requests_fake:
            requests_fake.return_value.ok = True

            for pessoa in self.pessoas:

                self.assertEqual(pessoa.obter_todos_os_dados(), 'Conectado')
                self.assertTrue(pessoa.dados_obtidos)

            requests_fake.return_value.ok = False

            self.assertEqual(pessoa.obter_todos_os_dados(), 'Erro 404')
            self.assertFalse(pessoa.dados_obtidos)


if __name__ == "__main__":
    unittest.main(verbosity=2)
