from parser import Parser
from unittest import TestCase

class Test_Parser_ConvertCurrentType(TestCase):

    def test_boolean_true(self):
        parser = Parser()
        result = parser.convertCurrentType("true")
        expectedResult = True
        self.assertEqual(result, expectedResult)

    def test_boolean_false(self):
        parser = Parser()
        result = parser.convertCurrentType("FALSE")
        expectedResult = False
        self.assertEqual(result, expectedResult)

    def test_int(self):
        parser = Parser()
        result = parser.convertCurrentType("24642")
        expectedResult = 24642
        self.assertEqual(result, expectedResult)
    
    def test_float(self):
        parser = Parser()
        result = parser.convertCurrentType("463.364336")
        expectedResult = 463.364336
        self.assertEqual(result, expectedResult)

    def test_string(self):
        parser = Parser()
        result = parser.convertCurrentType("vdg35v@.{2}s")
        expectedResult = "vdg35v@.{2}s"
        self.assertEqual(result, expectedResult)
