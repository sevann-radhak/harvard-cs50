import unittest
from jar import Jar

class TestJar(unittest.TestCase):
    def test_deposit(self):
        jar = Jar()
        jar.deposit(5)
        self.assertEqual(jar.size, 5)

    def test_withdraw(self):
        jar = Jar()
        jar.deposit(10)
        jar.withdraw(5)
        self.assertEqual(jar.size, 5)

    def test_over_deposit(self):
        jar = Jar()
        with self.assertRaises(ValueError):
            jar.deposit(13)

    def test_over_withdraw(self):
        jar = Jar()
        jar.deposit(5)
        with self.assertRaises(ValueError):
            jar.withdraw(6)

    def test_negative_deposit(self):
        jar = Jar()
        with self.assertRaises(ValueError):
            jar.deposit(-5)

    def test_negative_withdraw(self):
        jar = Jar()
        with self.assertRaises(ValueError):
            jar.withdraw(-5)

    def test_capacity(self):
        jar = Jar(20)
        self.assertEqual(jar.capacity, 20)

    def test_negative_capacity(self):
        with self.assertRaises(ValueError):
            Jar(-5)

    def test_str(self):
        jar = Jar()
        jar.deposit(5)
        self.assertEqual(str(jar), '🍪🍪🍪🍪🍪')
