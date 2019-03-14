import unittest
from calc import Calc


class TestCalc(unittest.TestCase):
    def test_valid_expressions(self):
        expression = "1+2*3-10/2"
        c = Calc(expression)
        expected = (5, "1+2*3-10/2", 1+2*3-10/2)
        actual = c.expression_result()
        self.assertEqual(actual, expected)

    def test_expressions_with_letter(self):
        expression = "1a+2*3-10/2"
        c = Calc(expression)
        expected = 'Expression contains nondigital symbol(s)'
        actual = c.expression_result()
        self.assertEqual(actual, expected)

    def test_expression_with_no_numbers(self):
        expression = "+-/*"
        c = Calc(expression)
        expected = 'Expression must contain minimum 2 numbers'
        actual = c.expression_result()
        self.assertEqual(actual, expected)

    def test_expression_with_one_number(self):
        expression = "/555"
        c = Calc(expression)
        expected = 'Expression must contain minimum 2 numbers'
        actual = c.expression_result()
        self.assertEqual(actual, expected)

    def test_expression_with_ten_numbers(self):
        pass

    def test_expression_with_more_then_ten_numbers(self):
        pass

    def test_expression_with_correct_parentheses(self):
        pass

    def test_expression_with_incorrect_parentheses(self):
        pass

if __name__ == '__main__':
    unittest.main()
