from taller4 import total, addit, mult, divide, length, reverse, remove_letter, even_numbers, odd_numbers, is_even
import unittest

print(" --------------------------- Pruebas Ejecutadas ---------------------------")

class TestTotal(unittest.TestCase):

    def testTotal_success(self):
        resultado = total([1, 2, 3])
        self.assertEqual(resultado, 6)
    
    def testTotal_assertIsNot(self):
        resultado = divide(8, 2)
        self.assertIsNot(type(resultado), str)

class TestAddit(unittest.TestCase):

    def testAddit_success(self):
        resultado = addit(3)
        self.assertEqual(resultado, 8)
    
    def testAddit_assertIsNone(self):
        resultado = addit(3)
        message = "Test value is not none."
        self.assertIsNone(resultado, message)


class TestAddit(unittest.TestCase):

    def testAddit_notEqual(self):
        resultado = addit(3)
        self.assertNotEqual(resultado, 7)
    
    def testAddit_assertIsNotNone(self):
        resultado = addit(3)
        self.assertIsNotNone(resultado, 7)

class TestMult(unittest.TestCase):

    def testMult_success(self):
        resultado = mult(1)
        self.assertEqual(resultado, 6)

class TestDivide(unittest.TestCase):

    def testDivide_success(self):
        resultado = divide(8, 2)
        self.assertEqual(resultado, 4)

    def testDivide_assertIs(self):
        resultado = divide(8, 2)
        self.assertIs(type(resultado), float)
        

class TestLength(unittest.TestCase):

    def testLength_success(self):
        resultado = length([2, 3, 5, 2, 6, 7, 8, 9, 10])
        self.assertEqual(resultado, "Longer than 5")

class TestReverse(unittest.TestCase):

    def testReverse_success(self):
        resultado = reverse("casa")
        self.assertEqual(resultado, "asac")

class TestRemoveLetter(unittest.TestCase):

    def testRemoveLetter_success(self):
        resultado = remove_letter("a", "ana maria")
        self.assertEqual(resultado, "n mri")
    
    def testRemoveLetter_assertIn(self):
        resultado = remove_letter("a", "ana maria")
        message = "key is not in container."
        self.assertIn("mri", resultado, message)
    
    def testRemoveLetter_assertNotIn(self):
        resultado = remove_letter("a", "ana maria")
        message = "key is not in container."
        self.assertNotIn("ana", resultado, message)
        

class TestMax(unittest.TestCase):

    def testMax_success(self):
        resultado = max(1, 2)
        self.assertEqual(resultado, 2)
    
    def testMax_assertIsInstance(self):
        resultado = max(1, 2)
        self.assertIsInstance(resultado, int)
    
    def testMax_assertNotIsInstance(self):
        resultado = max(1, 2)
        self.assertNotIsInstance(resultado, str)


class TestEvenNumbers(unittest.TestCase):

    def TestEvenNumbers_success(self):
        resultado = even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(resultado, [2, 4, 6, 8, 10])

class TestOddNumbers(unittest.TestCase):

    def testOddNumbers_success(self):
        resultado = odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(resultado, [1, 3, 5, 7, 9])

class TestIsEven(unittest.TestCase):

    def testIsEven_success(self):
        resultado = is_even(2)
        self.assertEqual(resultado, True)

    def testIsEven_assertTrue(self):
        resultado = is_even(2)
        self.assertTrue(resultado)

    def testIsEven_assertFalse(self):
        resultado = is_even(3)
        self.assertFalse(resultado)
    

if __name__ == '__main__':
    unittest.main()

