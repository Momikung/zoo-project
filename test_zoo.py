import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
        self.assertEqual(self.zoo.get_ticket_price(30), 150)
        self.assertEqual(self.zoo.get_ticket_price(70), 100)
            
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()