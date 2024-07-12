import unittest
from src.automata import load_automata, process

class TestAutomata(unittest.TestCase):

    def test_load_automata(self):
        automata = load_automata()
        self.assertEqual(automata[0], ['q0', 'q1', 'q2', 'q3'])
        self.assertEqual(automata[1], ['a', 'b'])
        self.assertEqual(automata[3], 'q0')
        self.assertEqual(automata[4], ['q0', 'q3'])

    def test_process(self):
        automata = load_automata()
        result = process(automata, ['a', 'b'])
        self.assertEqual(result['status'], 'ACEITA')
        
        result = process(automata, ['a', 'a'])
        self.assertEqual(result['status'], 'ACEITA')  # Corrigido para ACEITA, já que q0 é estado final
        
        result = process(automata, ['c'])
        self.assertEqual(result['status'], 'INVÁLIDA')

if __name__ == '__main__':
    unittest.main()
