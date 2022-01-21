import uuid
from django.test import TestCase
from model_bakery import baker

from core.models import get_file_path


class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTestCase(TestCase):

    def setUp(self):
        self.servico = baker.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)


class CartoTestCase(TestCase):

    def setUp(self):
        self.cargo = baker.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):

    def setUp(self):
        self.funcionario = baker.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)
