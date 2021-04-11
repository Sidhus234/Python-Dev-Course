import unittest
import mainI

class TestGame(unittest.TestCase):
    def test_input(self):
        result = mainI.run_guess(5, 5)
        self.assertTrue(result)
    
    def test_input_wrong_answer(self):
        result = mainI.run_guess(5, 10)
        self.assertFalse(result)
        
    def test_input_wrong_number(self):
        result = mainI.run_guess(5, 11)
        self.assertFalse(result)
        
    def test_input_wrong_type(self):
        result = mainI.run_guess(5, '10')
        self.assertFalse(result)
    

if __name__ == '__main__':
    unittest.main()