import unittest
from unittest import TestCase

from spiralPrint import spiralPrint

class TestSpiralPrint(unittest.TestCase):
    def test_matrix(self):
        self.assertEquals(spiralPrint('https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'),[
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
])