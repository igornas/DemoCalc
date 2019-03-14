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
        expression = "100+20*3-10/2+11-1*10+34-54"
        c = Calc(expression)
        expected = (10, "100+20*3-10/2+11-1*10+34-54", 100+20*3-10/2+11-1*10+34-54)
        actual = c.expression_result()
        self.assertEqual(actual, expected)

    def test_expression_with_more_then_ten_numbers(self):
        expression = "100+20*3-10/2+11-1*10+34-54+21"
        c = Calc(expression)
        expected = 'Expression contain more than 10 numbers'
        actual = c.expression_result()
        self.assertEqual(actual, expected)

    def test_expression_with_correct_parentheses(self):
        expression = "((100+20)*3-10/2+11-1*(10+34)-54)"
        c = Calc(expression)
        expected = (10, "((100+20)*3-10/2+11-1*(10+34)-54)", ((100+20)*3-10/2+11-1*(10+34)-54))
        actual = c.expression_result()
        self.assertEqual(actual, expected)

    def test_expression_with_incorrect_parentheses(self):
        expression = "((100+20)*3)-10/2+11-1*(10+34)-54)"
        c = Calc(expression)
        expected = 'Missing bracket(s)'
        actual = c.expression_result()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
