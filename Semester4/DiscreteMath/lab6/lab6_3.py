from lab6_1 import CalculateBit


class CalculateBitWithSheffer(CalculateBit):
    logic_constants = {
        '*': 'and',
        '+': 'or',
        '-': 'not',
        '^': 'not ({} or {})'
    }

    def value_from_logic_constants(self, symbol: str) -> str:
        if symbol != '^':
            return super().value_from_logic_constants(symbol)
        A = self.clear_formula.pop(-1)
        B = self.clear_formula.pop(-1)
        return self.logic_constants[symbol].format(A, B)


if __name__ == '__main__':
    constants = {
        'A': 0,
        'W': 0,
        'B': 1,
        'C': 1,
    }

    print(constants)
    bitcalculation = CalculateBitWithSheffer(constants)
    while True:
        formula = input('formula >>>')
        result = bitcalculation.result(formula)
        print(result, end='\n\n')
