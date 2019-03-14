import re


class Calc:

    _PATTERNS = {
        'INT': r'\d+',
        'FLOAT': r'\d+[\.,]\d+',
        'NONDIGIT': r'[a-zA-Z]',
        'LEFT_OP': r'\d+[(]',
        'RIGHT_OP': r'[)]\d+'
    }

    _STATUS = {
        '0': 'Expression contains nondigital symbol(s)',
        '1': 'Expression contains float number(s)',
        '2': 'Missing bracket(s)',
        '3': 'Expression contain more than 10 numbers',
        '4': 'Expression must contain minimum 2 numbers',
        '5': 'missing operator near parentheses',
    }

    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"Calc object with expression = {self.expression}"

    def check_round_brackets(self):
        return self.expression.count('(') != self.expression.count(')')

    def check_nondigit_symbols(self):
        return re.search(self._PATTERNS['NONDIGIT'], self.expression)

    def check_float_numbers(self):
        return re.search(self._PATTERNS['FLOAT'], self.expression)

    def check_qty_of_numbers(self):
        qty = len(re.findall(self._PATTERNS['INT'], self.expression))
        return qty

    def check_skip_operator(self):
        left =  re.search(self._PATTERNS['LEFT_OP'], self.expression)
        right = re.search(self._PATTERNS['RIGHT_OP'], self.expression)
        return left or right

    def expression_result(self):
        result = []

        if self.check_nondigit_symbols():
            return self._STATUS['0']

        if self.check_float_numbers():
            return self._STATUS['1']

        if self.check_round_brackets():
            return self._STATUS['2']

        if self.check_qty_of_numbers() > 10:
            return self._STATUS['3']

        if self.check_qty_of_numbers() < 2:
            return self._STATUS['4']

        if self.check_skip_operator():
            return self._STATUS['5']

        try:
            return self.check_qty_of_numbers(), self.expression, eval(self.expression)
        except ZeroDivisionError:
            return "Error. Your expression contains division by zero"


def main():
    expression = input("Type your expression for calculate: ")
    calc = Calc(expression)
    print(calc.expression_result())



if __name__ == '__main__':
    main()
