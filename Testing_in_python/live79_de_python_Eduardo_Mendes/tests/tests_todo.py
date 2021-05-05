from unittest import TestCase, mock
from datetime import datetime

# import sys
# sys.path.append('/home/wesley/Desktop/Wesley/Python_learnings/Testing_in_python/live_de_python_Eduardo_Mendes')
from app.todo import nova_task, process_date

'''
    Para rodar
    $ python3 -m unittest -v tests/tests_todo.py
'''

"""
    {
        'id': int,
        'task_name': str,
        'date': str,
        'state': str['TODO', 'Fazendo', 'Pronto']
    }
"""

class TestNovaTask(TestCase):

    def test_nova_task(self):
        esperado = {
        'id': 1,
        'task_name': 'str',
        'date': datetime(2019, 2, 19, 0, 0, 0),
        'state': 'TODO'
        }

        result = nova_task('Ligar pro Will','19/02/2019')

        self.assertEqual(esperado, result)

    @mock.patch('app.todo.process_date', return_value = 123) # Espião
    def test_process_date_deve_ser_chamado_com_19_02_2019(self, mocked):
        # Chama a função
        result = nova_task('', '19/02/2019') # Dummy, não foi passado nada
        
        # Garante que a função interna foi chamada
        mocked.assert_called_with('19/02/2019') # Espionar de foi chamada

        # Garantir se o resultado está no contexto
        self.assertEqual(result['date'], '19/02/2019')


class TestProcessDate(TestCase):

    def test_process_date_deve_converter_para_datetime_a_string_passada(self):
        """
        19/02/2019 -> datetime(2019, 2, 19, 0, 0, 0)
        """
        esperado = datetime(2019, 2, 19, 0, 0, 0)
        result = process_date('19/2/2019')

        self.assertEqual(esperado, result)