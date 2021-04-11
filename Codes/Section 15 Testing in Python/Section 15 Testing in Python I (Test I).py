import unittest
import main


class TestMain(unittest.TestCase):
    # setUp runs before every function
    def setUp(self):
        print('about to test a function')
    
    def test_do_stuff(self):
        """
        Just a test
        """
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff2(self):
        test_param = 'ashsd'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))
    
    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
        
    def test_do_Stuff4(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
    
    # run after each method is called
    def tearDown(self):
        print('cleaning up')

# Below line of code ensures that this only runs if we are running this file
if __name__ == '__main__':
    unittest.main()