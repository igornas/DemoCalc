import unittest
from calc import Calc


class TestCalc(unittest.TestCase):
    def test_create_object(self):

        c = Calc("123")
        expected = "123"
        self.assertEqual(c.expression, expected)
        expected = "Calc object with expression = 123"
        self.assertEqual(c.__repr__(), expected)

    def test_check_round_brackets(self):
        c1 = Calc("123+(12-3)*2")
        self.assertEqual(c1.check_round_brackets(), False)
        c2 = Calc("123+(12-3)*2)")
        self.assertEqual(c2.check_round_brackets(), True)

    def test_check_nondigit_symbols(self):
        c1 = Calc("123*2")
        self.assertEqual(c1.check_nondigit_symbols(), False)
        c2 = Calc("123sd*2)")
        self.assertEqual(c2.check_nondigit_symbols(), True)

    def test_check_float_numbers(self):
        c1 = Calc("54+123.345-2")
        self.assertEqual(c1.check_float_numbers(), True)
        c2 = Calc("54+123,345-2")
        self.assertEqual(c2.check_float_numbers(), True)
        c3 = Calc("54+123345-2")
        self.assertEqual(c3.check_float_numbers(), False)


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

    def test_expressions_with_floats(self):
        expression = "100+2.345*3-10/2"
        c1 = Calc(expression)
        expected = 'Expression contains float number(s)'
        actual = c1.expression_result()
        self.assertEqual(actual, expected)

        expression = "100,34+2*3-10/2"
        c2 = Calc(expression)
        expected = 'Expression contains float number(s)'
        actual = c2.expression_result()
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

    def test_expression_with_missing_operator(self):
        expression = "((100+20)3-10/2+11-1*(10+34)-54)"
        c1 = Calc(expression)
        expected = 'missing operator near parentheses'
        actual = c1.expression_result()
        self.assertEqual(actual, expected)

        expression = "((100+20)*3-10/2+11-2(10+34)-54)"
        c2 = Calc(expression)
        expected = 'missing operator near parentheses'
        actual = c2.expression_result()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
