from main import convertCurrentType
from unittest import TestCase, main

class TestConvertCurrentType(TestCase):

    def test_boolean_true(self):
        result = convertCurrentType("true")
        expectedResult = True
        self.assertEqual(result, expectedResult)

    def test_boolean_false(self):
        result = convertCurrentType("FALSE")
        expectedResult = False
        self.assertEqual(result, expectedResult)

    def test_int(self):
        result = convertCurrentType("24642")
        expectedResult = 24642
        self.assertEqual(result, expectedResult)
    
    def test_float(self):
        result = convertCurrentType("463.364336")
        expectedResult = 463.364336
        self.assertEqual(result, expectedResult)

    def test_string(self):
        result = convertCurrentType("vdg35v@.{2}s")
        expectedResult = "vdg35v@.{2}s"
        self.assertEqual(result, expectedResult)

if __name__ == '__main__':
    main()